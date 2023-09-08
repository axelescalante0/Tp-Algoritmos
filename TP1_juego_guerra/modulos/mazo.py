from TP1_LDE_testing.modulos.main import ListaDobleEnlazada
from random import randint

valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
palos = ["♠", "♥", "♦", "♣"]

#------------------------------------------------------------------------------------
class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        string = str(self.valor) + self.palo
        return string

#------------------------------------------------------------------------------------
class Mazo:
    def __init__(self):
        self.mazo = ListaDobleEnlazada()

    def generar_mazo(self):
        for palo in palos:
            for valor in valores:
                # if valor not in ['J','Q','K','A']:
                # valor = int(valor)
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
        carta = self.mazo.extraer(0)
        return carta
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
class JuegoGuerra:
    def __init__(self):
        self.turno = 0
        self.guerra = False
        self.mazo = Mazo()
        self.jugador_1 = Mazo()
        self.jugador_2 = Mazo()
        self.mesa = Mazo()

    def repartir(self):
        for i in range(1, 53):
            carta = self.mazo.sacar_arriba()
            if i % 2 == 0:
                self.jugador_1.poner_arriba(carta)
            else:
                self.jugador_2.poner_arriba(carta)

    def iniciar_guerra(self,carta_1,carta_2):
        self.mesa.poner_abajo(carta_1)
        self.mesa.poner_abajo(carta_2)
        if len(self.jugador_1.mazo) < 3 or len(self.jugador_2.mazo) < 3:
            return True
        for _ in range(3):
            self.mesa.poner_abajo(self.jugador_1.sacar_arriba())
            self.mesa.poner_abajo(self.jugador_2.sacar_arriba())

    def comparar_cartas(self, carta_1, carta_2):
        valor_1 = valores.index(carta_1.valor) + 2
        valor_2 = valores.index(carta_2.valor) + 2
        if valor_1 > valor_2:
            if not self.guerra:
                self.jugador_1.poner_abajo(carta_1)
                self.jugador_1.poner_abajo(carta_2)
            else:
                for _ in self.mesa.mazo:
                    self.jugador_1.poner_abajo(self.mesa.sacar_arriba())

                self.jugador_1.poner_abajo(carta_1)
                self.jugador_1.poner_abajo(carta_2)

                self.guerra = False

        elif valor_1 < valor_2:
            if not self.guerra:
                self.jugador_2.poner_abajo(carta_1)
                self.jugador_2.poner_abajo(carta_2)
            else:
                for _ in self.mesa.mazo:
                    self.jugador_1.poner_abajo(self.mesa.sacar_arriba())

                self.jugador_2.poner_abajo(carta_1)
                self.jugador_2.poner_abajo(carta_2)

                self.guerra = False
        else:
            self.guerra = True

    def iniciar_juego(self):

        self.mazo.mezclar()
        self.repartir()
        string_cartas = ""

        while self.turno <= 10000:

            if  self.jugador_1.mazo.tamanio == 0 or self.jugador_2.mazo.tamanio == 0:
                break

            carta_1 = self.jugador_1.sacar_arriba()
            carta_2 = self.jugador_2.sacar_arriba()
            

            #input("Presiona Enter para avanzar al siguiente turno...")

            # Este bloque imprimpe la interfaz
#------------------------------------------------------------------------------------
            print("--------------------------------------")

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

            if not self.guerra:
                string_cartas = carta_1.valor + carta_1.palo + " " + carta_2.valor + carta_2.palo
                print(" "*10, string_cartas)
            else:
                print(" "*10,string_cartas,"-X"*6, carta_1,"", carta_2)

            print("\n")
            print("Jugador 2:")
            # Imprimo las cartas boca abajo del mazo del jugador 2 según su cantidad
            for i in range(len(self.jugador_2.mazo)):
                if i % 10 == 0 and i != 0:
                    print()  # Salto de línea después de cada 10 cartas
                print("-X", end=" ")  # Imprimir carta, sin salto de línea

            print("\n--------------------------------------")
#------------------------------------------------------------------------------------
            self.turno += 1

            self.comparar_cartas(carta_1,carta_2)

            if self.guerra:
                if self.iniciar_guerra(carta_1,carta_2):
                    break

            # Verifica si el juego debe continuar
            if self.turno >= 10000:
                print("Empate")
                break

        if self.jugador_1.mazo.tamanio == 0:
            print(" "*8,"****** Jugador 2 gana la partida ******")
        elif self.jugador_2.mazo.tamanio == 0:
            print(" "*8, "****** Jugador 1 gana la partida ******")
        else:
            print("Hubo un problema en el juego")

jugar = JuegoGuerra()

jugar.iniciar_juego()
