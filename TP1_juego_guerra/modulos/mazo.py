from TP1_LDE_testing.modulos.main import ListaDobleEnlazada
from random import randint

valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
palos = ["♠", "♥", "♦", "♣"]


class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        string = str(self.valor) + self.palo
        return string


class Mazo:
    def __init__(self):
        self.mazo = ListaDobleEnlazada()
        self.guerra = False

    def generar_mazo(self):
        for palo in palos:
            for valor in valores:
                # if valor not in ['J','Q','K','A']:
                # valor = int(valor)
                self.mazo.agregar_al_final(Carta(valor, palo))

    def mezclar(self):
        self.generar_mazo()
#                           IMPLEMENTAR OTRA FORMA DE MEZCLAR
#------------------------------------------------------------------------------------
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
        self.generar_mazo()
#------------------------------------------------------------------------------------
    def poner_arriba(self, carta):
       self.mazo.agregar_al_inicio(carta)

    def poner_abajo(self, carta):
        self.mazo.agregar_al_final(carta) 

    def sacar_arriba(self):
        carta = self.mazo.extraer(0)
        return carta


class JuegoGuerra:
    def __init__(self):
        self.turno = 0
        self.guerra = False
        self.mazo = Mazo()
        self.jugador_1 = Mazo()
        self.jugador_2 = Mazo()
        self.mazo_guerra = Mazo()
        self.finalizado = True

    def repartir(self):
        for i in range(1, 53):
            carta = self.mazo.sacar_arriba()
            if i % 2 == 0:
                self.jugador_1.poner_arriba(carta)
            else:
                self.jugador_2.poner_arriba(carta)

    def guerra_M(self,carta_1,carta_2):
        self.mazo_guerra.poner_abajo(carta_1)
        self.mazo_guerra.poner_abajo(carta_2)

        for _ in range(3):
            if len(self.jugador_1.mazo) < 3 or len(self.jugador_2.mazo) < 3:
                break
            else:
                self.mazo_guerra.poner_abajo(self.jugador_1.sacar_arriba())
                self.mazo_guerra.poner_abajo(self.jugador_2.sacar_arriba())


    def rondas(self, carta_1, carta_2):
        valor_1 = valores.index(carta_1.valor) + 2
        valor_2 = valores.index(carta_2.valor) + 2
        if valor_1 > valor_2:
            if not self.guerra:
                self.jugador_1.poner_abajo(carta_1)
                self.jugador_1.poner_abajo(carta_2)
            else:
                for _ in self.mazo_guerra.mazo:
                    self.jugador_1.poner_abajo(self.mazo_guerra.sacar_arriba())

                self.jugador_1.poner_abajo(carta_1)
                self.jugador_1.poner_abajo(carta_2)

                self.guerra = False

        elif valor_1 < valor_2:
            if not self.guerra:
                self.jugador_2.poner_abajo(carta_1)
                self.jugador_2.poner_abajo(carta_2)
            else:
                for _ in self.mazo_guerra.mazo:
                    self.jugador_1.poner_abajo(self.mazo_guerra.sacar_arriba())

                self.jugador_2.poner_abajo(carta_1)
                self.jugador_2.poner_abajo(carta_2)

                self.guerra = False
        else:
            self.guerra = True

    def iniciar_juego(self):

        self.mazo.mezclar()
        self.repartir()

        string_cartas = ""
        while self.finalizado:

            if  self.jugador_1.mazo.tamanio == 0 or self.jugador_2.mazo.tamanio == 0:
                break

            carta_1 = self.jugador_1.sacar_arriba()
            carta_2 = self.jugador_2.sacar_arriba()
            

            #input("Presiona Enter para avanzar al siguiente turno...")
            print("--------------------------------------")

            if self.guerra:
                print("                   **** Guerra!! ****")
            print("Turno: ", self.turno)
            print("Jugador 1:")
            for i in range(len(self.jugador_1.mazo)):
                if i % 10 == 0 and i != 0:
                    print()  # Salto de línea después de cada 10 cartas
                print("-X", end=" ")  # Imprimir carta, sin salto de línea

            print("\n")

            if not self.guerra:
                string_cartas = carta_1.valor + carta_1.palo + " " + carta_2.valor + carta_2.palo
                print(" "*10, string_cartas)
            else:
                print(" "*10,string_cartas,"-X"*6, carta_1," ", carta_2)

            print("\n")
            print("Jugador 2:")
            for i in range(len(self.jugador_2.mazo)):
                if i % 10 == 0 and i != 0:
                    print()  # Salto de línea después de cada 10 cartas
                print("-X", end=" ")  # Imprimir carta, sin salto de línea

            print("\n--------------------------------------")
            self.turno += 1

            self.rondas(carta_1,carta_2)

            if self.guerra:
                self.guerra_M(carta_1,carta_2)
            # Verifica si el juego debe continuar
            if self.turno >= 10000:
                self.finalizado = False

        if self.turno >= 10000:
            print("Empate")
        elif self.jugador_1.mazo.tamanio == 0:
            print(" "*8,"****** Jugador 2 gana la partida ******")
        elif self.jugador_2.mazo.tamanio == 0:
            print(" "*8, "****** Jugador 1 gana la partida ******")
        else:
            print("Hubo un problema en el juego")

# jugar = JuegoGuerra()

# jugar.iniciar_juego()

# print("Mazo jugador 1 --->",jugar.jugador_1.mazo, jugar.jugador_1.mazo.tamanio)
# print("Mazo jugador 2 --->",jugar.jugador_2.mazo, jugar.jugador_2.mazo.tamanio)