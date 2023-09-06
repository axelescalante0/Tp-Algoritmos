from TP1_juego_guerra.modulos.mazo import Mazo, Carta
import unittest


class TestMazo(unittest.TestCase):
    def setUp(self):
        self.mazo= Mazo()

# Chequeo de repartir/poner arriba, sacar arriba/principio y poner abajo/final
    def test_poner_sacar_arriba(self):            #Poner arriba al momento de repartir las cartas, sacar arriba al momento de jugar el turno
        carta1=Carta('5','trebol')
        carta2=Carta('3','corazones')
        self.mazo.poner_arriba(carta1)
        self.mazo.poner_arriba(carta2)
        self.assertIs(carta2, self.mazo.mazo.items[0])
        carta_control=self.mazo.sacar_arriba()
        self.assertIs(carta2, carta_control)

    def test_poner_abajo(self):                     #Poner abajo al momento de ganar el turno
        carta1=Carta('5','trebol')
        carta2=Carta('3','corazones')
        self.mazo.poner_abajo(carta1)
        self.mazo.poner_abajo(carta2)
        self.assertIs(carta2, self.mazo.mazo.items[-1])
        
if __name__ == '__main__':
    unittest.main()
