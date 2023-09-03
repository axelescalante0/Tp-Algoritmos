#esta_vacia(): Devuelve True si la lista está vacía. 
#tamanio(): Devuelve el número de ítems de la lista.
#agregar_al_inicio(item): Agrega un nuevo ítem al inicio de la lista.
#agregar_al_final(item): Agrega un nuevo ítem al final de la lista.
#insertar(item, posicion): Agrega un nuevo ítem a la lista en "posicion".
#        Si la posición no se pasa como argumento, el ítem debe añadirse al final de la lista. "posicion" 
#        es un entero que indica la posición en la lista donde se va a insertar el nuevo elemento.
#extraer(posicion): elimina y devuelve el ítem en "posición". Si no se indica el parámetro posición,
#        se elimina y devuelve el último elemento de la lista.
#copiar(): Realiza una copia de la lista elemento a elemento y devuelve la copia.
#invertir(): Invierte el orden de los elementos de la lista.
#ordenar(): Ordena los elementos de la lista de "menor a mayor".
#concatenar(Lista): Recibe una lista como argumento y retorna la lista actual con la lista pasada como
#        parámetro concatenada al final de la primera. Esta operación también debe ser posible utilizando el operador 
#        de suma ‘+’. Aclaración: No se deben modificar las listas.

class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None
        
class ListaDobleEnlazada:

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def estaVacia(self):
        return self.cabeza == None

    def agregar_al_inicio(self, item):
        nuevo_nodo = Nodo(item)
        if self.estaVacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, item):
        nuevo_nodo = Nodo(item)
        if self.estaVacia():
            self.cabeza = self.cola = Nodo(item)
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        if posicion == None or posicion >= self.tamanio:
            self.agregar_al_final(item)
        elif posicion == 0 or self.estaVacia():
            self.agregar_al_inicio(item)
        elif posicion < 0:
            raise RuntimeError("Usted no puede usar un número negativo para la posición")
        else:
            nuevo_nodo = Nodo(item)
            nodo_anterior = self.cabeza
            for _ in range(1,posicion):
                nodo_anterior = nodo_anterior.siguiente

            nodo_siguiente = nodo_anterior.siguiente  
            nuevo_nodo.siguiente = nodo_siguiente
            nuevo_nodo.anterior = nodo_anterior
            nodo_anterior.siguiente = nuevo_nodo
            nodo_siguiente.anterior = nuevo_nodo
            self.tamanio += 1
    
    def concatenar(self,lista):
        lista_2_copia = lista.copiar()
        cabeza_lista_2 = lista_2_copia.cabeza
        ultimo_nodo_lista_1 = self.cola

        ultimo_nodo_lista_1.siguiente = cabeza_lista_2
        cabeza_lista_2.anterior = ultimo_nodo_lista_1
        self.cola = lista_2_copia.cola

        self.tamanio += len(lista)

    def extraer(self,posicion = None):
        if self.tamanio == 0:
            raise RuntimeError("Lista vacía")
        elif posicion == None and self.tamanio == 1:
            dato = self.cabeza.dato
            self.cabeza = self.cola = None
            self.tamanio = 0
        elif posicion == 0 and self.tamanio > 1:
            dato = self.cabeza.dato
            nodo_segundo = self.cabeza.siguiente
            nodo_segundo.anterior = None
            self.cabeza = nodo_segundo
            self.tamanio -= 1                
        elif (posicion == None or posicion == self.tamanio-1 or posicion == -1) and self.tamanio > 1:
            dato = self.cola.dato
            nodo_ante_ultimo = self.cola.anterior
            nodo_ante_ultimo.siguiente = None
            
            self.cola = nodo_ante_ultimo

            self.tamanio -= 1
        else:
            nodo_extraer = self.cabeza
            for _ in range(posicion):
                nodo_extraer = nodo_extraer.siguiente
            dato = nodo_extraer.dato
            # obtengo los nodos que están conectados al que quiero eliminar
            #nodo_siguiente = nodo_extraer.siguiente
            #nodo_anterior = nodo_extraer.anterior
            # conecto los nodos
            #nodo_anterior.siguiente = nodo_siguiente
            #nodo_siguiente.anterior = nodo_anterior
            nodo_extraer.anterior.siguiente = nodo_extraer.siguiente
            nodo_extraer.siguiente.anterior = nodo_extraer.anterior
            self.tamanio -= 1

        return dato
    
    def invertir(self):
        nodo = self.cabeza
        i = self.tamanio
        for _ in range(i):
            item = nodo.dato
            self.agregar_al_inicio(item)
            nodo = nodo.siguiente
 
        for _ in range(i):    
            self.extraer()

    def tamano(self):
        return self.tamanio
    
    def copiar(self):
        copia_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual != None:
            copia_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia_lista

    def ordenar(self):
        # Primera llamada a otro metodo, pasandole la posicion 0 que será la cabeza del nodo
        # y el final que sería la cola
        if not self.estaVacia():
            self.ordenar_auxiliar(0,self.tamanio-1)
        else:
            raise RuntimeError("Lista vacía") 

    def ordenar_auxiliar(self,primero,ultimo):
        if primero < ultimo:
            # Lo segundo es llamar a la función quick_sort que va a ordenar y retornar
            # un punto para dividir la lista
            puntoDivision = self.particion(primero,ultimo)
            # Luego de dividir la lista, se llama a si misma para repetir el proceso de puntoDivision pero en
            # la primera mitad
            self.ordenar_auxiliar(primero,puntoDivision-1)
            # Por ultimo, se llama de nuevo pero se invierten los valores para que ordene la segunda mitad
            self.ordenar_auxiliar(puntoDivision+1,ultimo)

    def particion(self,primero,ultimo):
        if primero == 0 and ultimo == self.tamanio-1:
            nodo_pivote = self.cabeza
            nodo_Izq = self.cabeza.siguiente
            nodo_Der = self.cola
        else:
            if primero < (self.tamanio/2):
                nodo_pivote = self.cabeza
                for _ in range(primero):
                    nodo_pivote = nodo_pivote.siguiente
                nodo_Izq = nodo_pivote.siguiente
            else:
                nodo_pivote = self.cola
                for _ in range(((self.tamanio - 1) - primero)):
                    nodo_pivote = nodo_pivote.anterior
                nodo_Izq = nodo_pivote.siguiente

            if ultimo > (self.tamanio/2):
                nodo_Der = self.cola
                for _ in range(((self.tamanio - 1) - ultimo)):
                    nodo_Der = nodo_Der.anterior
            else:
                nodo_Der = self.cabeza
                for _ in range(ultimo):
                    nodo_Der = nodo_Der.siguiente

        marcaIzq = primero + 1
        marcaDer = ultimo

        hecho = False
        while not hecho:

            while marcaIzq <= marcaDer and nodo_Izq.dato <= nodo_pivote.dato:
                nodo_Izq = nodo_Izq.siguiente
                marcaIzq += 1
            while nodo_Der.dato >= nodo_pivote.dato and marcaDer >= marcaIzq:
                nodo_Der = nodo_Der.anterior
                marcaDer -=1

            if marcaDer < marcaIzq:
                hecho = True

            else:
                dato_Temp = nodo_Izq.dato
                nodo_Izq.dato = nodo_Der.dato
                nodo_Der.dato = dato_Temp

        dato_Temp = nodo_pivote.dato
        nodo_pivote.dato = nodo_Der.dato
        nodo_Der.dato = dato_Temp

        return marcaDer

    def __len__(self):
        return self.tamanio

    def __add__(self,lista):
        lista_concatenada = ListaDobleEnlazada()
        nodo_lista_1 = self.cabeza
        while nodo_lista_1 != None:
            lista_concatenada.agregar_al_final(nodo_lista_1.dato)
            nodo_lista_1 = nodo_lista_1.siguiente
        
        lista_concatenada.concatenar(lista)
        return lista_concatenada

    def __iter__(self):
            nodo= self.cabeza
            while nodo != None:
                yield(nodo.dato)
                nodo= nodo.siguiente
    # def __str__(self):
    #     string = ""
    #     nodo = self.cabeza
    #     while nodo != None:
    #         string += str(nodo.dato)
    #         string += " "
    #         nodo = nodo.siguiente
    #     return string