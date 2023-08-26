#esta_vacia(): Devuelve True si la lista está vacía. -------------
#tamanio(): Devuelve el número de ítems de la lista. -------------
#agregar_al_inicio(item): Agrega un nuevo ítem al inicio de la lista. -------------
#agregar_al_final(item): Agrega un nuevo ítem al final de la lista. -------------
#insertar(item, posicion): Agrega un nuevo ítem a la lista en "posicion". -------------
#        Si la posición no se pasa como argumento, el ítem debe añadirse al final de la lista. "posicion" 
#        es un entero que indica la posición en la lista donde se va a insertar el nuevo elemento.
#extraer(posicion): elimina y devuelve el ítem en "posición". Si no se indica el parámetro posición, -------------
#        se elimina y devuelve el último elemento de la lista.
#copiar(): Realiza una copia de la lista elemento a elemento y devuelve la copia. -------------
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
        self.size = 0

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
        self.size += 1

    def agregar_al_final(self, item):
        nuevo_nodo = Nodo(item)
        if self.estaVacia():
            self.cabeza = self.cola = Nodo(item)
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.size += 1

    def insertar(self, item, posicion=None):
        if posicion == None or posicion >= self.size:
            self.agregar_al_final(item)
        elif posicion == 0 or self.estaVacia() or posicion*-1 >= self.size:
            self.agregar_al_inicio(item)
        elif posicion < 0:
            posicion *= -1
            nuevo_nodo = Nodo(item)
            nodo_siguiente = self.cola
            for _ in range(posicion - 1):
                nodo_siguiente = nodo_siguiente.anterior

            nodo_anterior = nodo_siguiente.anterior
            nuevo_nodo.siguiente = nodo_siguiente
            nuevo_nodo.anterior = nodo_anterior
            nodo_anterior.siguiente = nuevo_nodo
            nodo_siguiente.anterior = nuevo_nodo

            self.size += 1
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

            self.size += 1
    
    def concatenar(self,lista):
        nodo_lista = lista.cabeza
        self.cola.siguiente = nodo_lista
        nodo_lista.anterior = self.cola
        self.cola = lista.cola
        self.size += lista.tamano()
    
    def extraer(self,posicion = None):

        if self.size == 0:
            return print("Lista vacía")
        elif posicion == None and self.size == 1:
            self.cabeza = self.cola = None
            self.size = 0
        elif posicion == None and self.size > 1:
            nodo_ante_ultimo = self.cola.anterior
            nodo_ante_ultimo.siguiente = None
            self.size -= 1
        elif posicion == 1 and self.size > 1:
            nodo_segundo = self.cabeza.siguiente
            self.cabeza = None
            self.cabeza = nodo_segundo
            self.size -= 1        
        else:
            nodo_extraer = self.cabeza
            for _ in range(posicion-1):
                nodo_extraer = nodo_extraer.siguiente

            nodo_siguiente = nodo_extraer.siguiente
            nodo_anterior = nodo_extraer.anterior
            nodo_anterior.siguiente = nodo_siguiente
            nodo_siguiente.anterior = nodo_anterior
            self.size -= 1

    def tamano(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        string = ""
        nodo = self.cabeza
        while nodo != None:
            string += str(nodo.dato)
            string += " "
            nodo = nodo.siguiente
        return string
    
    def __add__(self,lista):
        return self.concatenar(lista)
    
    def copiar(self):
        copia_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual != None:
            copia_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia_lista