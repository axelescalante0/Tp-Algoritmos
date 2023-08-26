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
        if posicion == None or posicion >= self.size or posicion == -1:
            self.agregar_al_final(item)
        elif posicion == 0 or self.estaVacia():
            self.agregar_al_inicio(item)
        else:
            nuevo_nodo = Nodo(item)
            nodo_anterior = self.cabeza
            for _ in range(posicion - 1):
                nodo_anterior = nodo_anterior.siguiente

            nodo_siguiente = nodo_anterior.siguiente  
            nuevo_nodo.siguiente = nodo_siguiente
            nuevo_nodo.anterior = nodo_anterior
            nodo_anterior.siguiente = nuevo_nodo
            nodo_siguiente.anterior = nuevo_nodo
            # Verificación de la conexión del nodo siguiente
            if nuevo_nodo.siguiente is not None:
                if nuevo_nodo.siguiente.anterior != nuevo_nodo:
                    print("Error: nodo siguiente no conectado correctamente")
            
            # Verificación de la conexión del nodo anterior
            if nodo_siguiente is not None:
                if nodo_siguiente.anterior != nuevo_nodo:
                    print("Error: nodo anterior no conectado correctamente")

            self.size += 1
    
    def concatenar(self,lista):
        nodo_lista = lista.cabeza
        self.cola.siguiente = nodo_lista
        nodo_lista.anterior = self.cola
        self.size += lista.tamano()
    def __str__(self):
        return str(self.size)
    
    def mostrar(self):
        string = ""
        nodo = self.cabeza
        while nodo != None:
            string += str(nodo.dato)
            string += " "
            nodo = nodo.siguiente
        return string
    
    def copiar(self):
        copia_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual != None:
            copia_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia_lista

lista = ListaDobleEnlazada()

lista.agregar_al_final(1)
lista.agregar_al_final(2)
lista.agregar_al_final(3)
lista.agregar_al_final(4)
lista.agregar_al_final(5)
lista.insertar(8)
lista.insertar(6,3)
lista.insertar(8,20)
lista.insertar(8,1)
lista.agregar_al_inicio(20)

print("Tamaño lista: ",lista.tamano())
print(lista.mostrar())

lista2 = ListaDobleEnlazada()
lista2.agregar_al_final(50)
lista2.agregar_al_final(100)
lista2.agregar_al_final(23)
lista2.agregar_al_final(59)

print("Tamaño lista2: ",lista2.tamano())
print("Lista2: ",lista2.mostrar())

lista.concatenar(lista2)

print("tamaño lista ",lista.tamano())
print("Lista concatenada ",lista.mostrar())


lista.insertar(200,12)
print("tamaño lista ",lista.tamano())
print("Lista concatenada ",lista.mostrar())