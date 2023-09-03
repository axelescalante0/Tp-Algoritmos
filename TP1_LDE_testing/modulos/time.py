import random
import timeit
import matplotlib.pyplot as plt
from main import ListaDobleEnlazada

def generar_lista_aleatoria(n):
    return [random.randint(1, 1000) for _ in range(n)]

def medir_tiempo_quick_sort(lista):
    inicio = timeit.default_timer()
    lista.ordenar()
    fin = timeit.default_timer()
    return fin - inicio

tamanios = [10, 100,250,500,750, 1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]  # Ajusta estos tamaños según tus necesidades
tiempos = []

for n in tamanios:
    lista = ListaDobleEnlazada()
    lista_datos = generar_lista_aleatoria(n)
    for dato in lista_datos:
        lista.agregar_al_final(dato)
    
    tiempo_ejecucion = medir_tiempo_quick_sort(lista)
    tiempos.append(tiempo_ejecucion)

plt.plot(tamanios, tiempos, marker='o', linestyle='-')
plt.xlabel('Tamaño de la Lista')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Medición de Tiempos de Ejecución del Método QuickSort')
plt.grid(True)
plt.show()