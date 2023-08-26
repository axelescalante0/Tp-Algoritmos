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
        self.size += lista.tamano()
    def tamano(self):
        return self.size
    
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