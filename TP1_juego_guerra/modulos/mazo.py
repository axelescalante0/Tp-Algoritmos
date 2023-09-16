from TP1_LDE_testing.modulos.main import ListaDobleEnlazada
from random import randint

#------------------------------------------------------------------------------------
valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
palos = ["♠", "♥", "♦", "♣"]
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return str(self.valor) + str(self.palo)

    def __repr__(self):
        return self.__str__()
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
class Mazo:
    def __init__(self):
        self.mazo = ListaDobleEnlazada()

    def generar_mazo(self):
        for palo in palos:
            for valor in valores:
                self.mazo.agregar_al_final(Carta(valor, palo))

    def mezclar(self):
        self.generar_mazo()
        mazo_1 = ListaDobleEnlazada()
        mazo_2 = ListaDobleEnlazada()
        for i, carta in enumerate(self.mazo):
            if i < 26:
                mazo_1.agregar_al_final(carta)
            else:
                mazo_2.agregar_al_final(carta)
        mazo_1.invertir()
        for i, carta in enumerate(mazo_1):
            mazo_2.insertar(carta, randint(0, 51))
        self.mazo = mazo_2.copiar()

    def poner_arriba(self, carta):
       self.mazo.agregar_al_inicio(carta)

    def poner_abajo(self, carta):
        self.mazo.agregar_al_final(carta) 

    def sacar_arriba(self):
        return self.mazo.extraer(0)
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
class JuegoGuerra:
    def __init__(self):
        self.turno = 1
        self.guerra = False
        self.mazo = Mazo()
        self.jugador_1 = Mazo()
        self.jugador_2 = Mazo()
        self.mesa = Mazo()
        self.string_cartas = ""

    def repartir(self):
        for i in range(1, 53):
            carta = self.mazo.sacar_arriba()
            # Se reparte de una forma intercalada, por lo que nunca se le 
            # va a repartir 2 cartas seguidas a un mismo jugador
            if i % 2 == 0:
                self.jugador_1.poner_arriba(carta)
            else:
                self.jugador_2.poner_arriba(carta)

    def iniciar_guerra(self,carta_1,carta_2):
        self.mesa.poner_abajo(carta_1)
        self.mesa.poner_abajo(carta_2)
        # Se comprueba si los mazos tienen suficientes cartas
        if len(self.jugador_1.mazo) < 4 or len(self.jugador_2.mazo) < 4:
            return True
        for _ in range(3):
            self.mesa.poner_abajo(self.jugador_1.sacar_arriba())
            self.mesa.poner_abajo(self.jugador_2.sacar_arriba())

    def comparar_cartas(self, carta_1, carta_2):
        valor_1 = valores.index(carta_1.valor) + 2
        valor_2 = valores.index(carta_2.valor) + 2
        # Se comparan los valores para saber el ganador
        if valor_1 > valor_2:
            # En el caso de que se inicie una guerra (guerra = True) y valor_1 > valor_2
            # se le repartirian las cartas al jugador correspondiente (jugador_1 en este caso)
            if self.guerra:
                for _ in self.mesa.mazo:
                    self.jugador_1.poner_abajo(self.mesa.sacar_arriba())
                self.jugador_1.poner_abajo(carta_1)
                self.jugador_1.poner_abajo(carta_2)
                # Después de que repartir las cartas, se cambia el estado de la guerra
                self.guerra = False
                self.string_cartas = ""
            # Si guerra = Flase se ejecutaría el else y se reparte normal
            else:
                self.jugador_1.poner_abajo(carta_1)
                self.jugador_1.poner_abajo(carta_2)

        elif valor_1 < valor_2:
            if self.guerra:
                for _ in self.mesa.mazo:
                    self.jugador_2.poner_abajo(self.mesa.sacar_arriba())
                self.jugador_2.poner_abajo(carta_1)
                self.jugador_2.poner_abajo(carta_2)
                self.guerra = False
                self.string_cartas = ""
            else:
                self.jugador_2.poner_abajo(carta_1)
                self.jugador_2.poner_abajo(carta_2)
        # En el caso de que no haya ganador, se cambia el estado de guerra y 
        # posteriormente entra en el metodo iniciar_guerra
        else:
            self.guerra = True

    def iniciar_juego(self):
        self.mazo.mezclar()
        self.repartir()

        while self.turno <= 10000:
            # Se comprueba constantemente el tamaño de los mazos
            if  self.jugador_1.mazo.tamanio == 0 or self.jugador_2.mazo.tamanio == 0:
                break
            # En cada turno se sacan las cartas a los jugadores para poder mostrarlas y compararlas
            carta_1 = self.jugador_1.sacar_arriba()
            carta_2 = self.jugador_2.sacar_arriba()

            # input("Presiona Enter para avanzar al siguiente turno...")
                            # Este bloque imprimpe la interfaz
            #------------------------------------------------------------------------
            print("--------------------------------------")

            # Si guerra = True se muestra el cartel de guerra
            if self.guerra:
                print(" "*20,"**** Guerra!! ****")

            print("Turno: ", self.turno)
            print("Jugador 1:")
            # Imprimo las cartas boca abajo del mazo del jugador 1 según su cantidad
            for i in range(len(self.jugador_1.mazo)):
                if i % 10 == 0 and i != 0:
                    print()  # Salto de línea después de cada 10 cartas
                print("-X", end=" ")  # Imprimir carta, sin salto de línea

            print("\n")
            # Cuando hay guerra se muestran todas las cartas
            if self.guerra:
                self.string_cartas += " " + "-X"*6+ " " + str(carta_1) + " " + str(carta_2)
                print(" "*10,self.string_cartas)
            # Y si no hay guerra, se guarda en string_cartas lo cual ayuda en el momento de guerra
            else:
                self.string_cartas = str(carta_1) + " " + str(carta_2)
                print(" "*10, self.string_cartas)

            print("\n")
            print("Jugador 2:")
            # Imprimo las cartas boca abajo del mazo del jugador 2 según su cantidad
            for i in range(len(self.jugador_2.mazo)):
                if i % 10 == 0 and i != 0:
                    print()  # Salto de línea después de cada 10 cartas
                print("-X", end=" ")  # Imprimir carta, sin salto de línea

            print("\n--------------------------------------")
            #------------------------------------------------------------------------
            self.turno += 1
            # Primero compara las cartas
            self.comparar_cartas(carta_1,carta_2)
            # Y después comprueba si guerra cambió a True
            if self.guerra:
                # En el caso de que uno de los mazos no tenga suficientes cartas
                # devuelve True y se rompe el while
                if self.iniciar_guerra(carta_1,carta_2):
                    break

        else:
            return print(" "*16+"****** Empate ******")
        # Si el mazo del jugador_1 == 0 o el mismo posea menos cartas que el jugador_2
        # (en el caso de que entren en guerra y tenga menos de 4 cartas) gana el 2
        if self.jugador_1.mazo.tamanio == 0 or self.jugador_2.mazo.tamanio > self.jugador_1.mazo.tamanio:
            print(" "*8,"****** Jugador 2 gana la partida ******")
        elif self.jugador_2.mazo.tamanio == 0 or self.jugador_1.mazo.tamanio > self.jugador_2.mazo.tamanio:
            print(" "*8, "****** Jugador 1 gana la partida ******")

#------------------------------------------------------------------------------------

# jugar = JuegoGuerra()
# jugar.iniciar_juego()