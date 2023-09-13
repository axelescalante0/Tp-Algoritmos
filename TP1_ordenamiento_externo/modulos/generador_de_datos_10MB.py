# -*- coding: utf-8 -*-
from random import randint
import os

def crear_archivo_de_datos(nombre):
    f = 10**6
    N = 5*f
    cifras = 20
    tam_bloque = f # 1 M de valores por bloque a escribir
    
    print('Cantidad de valores a escribir:', N)
    
    # truncar archivo si existe
    with open(nombre, 'w') as archivo:
        pass
    
    # escribir datos
    N_restantes = N
    while N_restantes > 0:
        cif = cifras
        r = N_restantes % tam_bloque
        c = N_restantes // tam_bloque
        if c > 0:
            t = tam_bloque
        elif c == 0:
            t = r
        N_restantes -= t
        print('t =', t, ', N_restantes =', N_restantes)
        bloque = [str(randint(10**(cif-1), 10**cif-1))+'\n'
                  for i in range(t)]        
        with open(nombre, 'a+') as archivo:
            archivo.writelines(bloque)
            
crear_archivo_de_datos('datos.txt')

def ordenamiento_por_mezcla(una_lista):
    # Implementa tu función de ordenamiento por mezcla aquí

    if len(una_lista) > 1:
        mitad = len(una_lista) // 2
        mitad_izquierda = una_lista[:mitad]
        mitad_derecha = una_lista[mitad:]

        ordenamiento_por_mezcla(mitad_izquierda)
        ordenamiento_por_mezcla(mitad_derecha)

        i = 0
        j = 0
        k = 0
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                una_lista[k] = mitad_izquierda[i]
                i = i + 1
            else:
                una_lista[k] = mitad_derecha[j]
                j = j + 1
            k = k + 1

        while i < len(mitad_izquierda):
            una_lista[k] = mitad_izquierda[i]
            i = i + 1
            k = k + 1

        while j < len(mitad_derecha):
            una_lista[k] = mitad_derecha[j]
            j = j + 1
            k = k + 1

def combinar_archivos_ordenados(lista_archivos, archivo_salida):
    # Combina los archivos ordenados en uno solo
    # lista_archivos es una lista de nombres de archivos ordenados
    # archivo_salida es el nombre del archivo de salida

    # Abre los archivos de entrada y el archivo de salida
    archivos_entrada = [open(archivo, 'r') for archivo in lista_archivos]
    salida = open(archivo_salida, 'w')

    # Lee la primera línea de cada archivo
    lineas = [archivo.readline().strip() for archivo in archivos_entrada]

    while any(lineas):
        # Encuentra el mínimo entre las líneas
        linea_minima = min(lineas)
        salida.write(linea_minima + '\n')

        # Encuentra el archivo que contenía la línea mínima y lee la siguiente línea
        indice_min = lineas.index(linea_minima)
        lineas[indice_min] = archivos_entrada[indice_min].readline().strip()

    # Cierra todos los archivos
    for archivo in archivos_entrada:
        archivo.close()
    salida.close()

# Dividir el archivo original en bloques más pequeños
tamaño_bloque = 10**6

with open('datos.txt', 'r') as archivo_original:
    lineas = archivo_original.readlines()
    for i in range(0, len(lineas), tamaño_bloque):
        bloque = lineas[i:i + tamaño_bloque]
        ordenamiento_por_mezcla(bloque)
        with open(f'bloque_{i // tamaño_bloque}.txt', 'w') as archivo_bloque:
            archivo_bloque.writelines(bloque)

# Obtener la lista de archivos ordenados
archivos_ordenados = [f'bloque_{i}.txt' for i in range(len(lineas) // tamaño_bloque)]

# Fusionar los archivos ordenados en uno solo
combinar_archivos_ordenados(archivos_ordenados, 'datos.txt')

# Eliminar los archivos temporales
for archivo in archivos_ordenados:
    os.remove(archivo)