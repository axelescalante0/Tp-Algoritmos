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

def ordenamientoRapido(unaLista):
   ordenamientoRapidoAuxiliar(unaLista,0,len(unaLista)-1)

def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo):
   if primero<ultimo:

       puntoDivision = particion(unaLista,primero,ultimo)

       ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
       ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)

def particion(unaLista,primero,ultimo):
   valorPivote = unaLista[primero]

   marcaIzq = primero+1
   marcaDer = ultimo

   hecho = False
   while not hecho:

       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1

       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = unaLista[marcaIzq]
           unaLista[marcaIzq] = unaLista[marcaDer]
           unaLista[marcaDer] = temp

   temp = unaLista[primero]
   unaLista[primero] = unaLista[marcaDer]
   unaLista[marcaDer] = temp

   return marcaDer

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

def merge_blocks(input_files, output_file):
    # Abre los archivos de entrada de los bloques
    file_handles = [open(file, 'r') for file in input_files]
    lines = [file.readline().strip() for file in file_handles]

    while any(lines):
        # Convierte las líneas en números enteros y omite las líneas vacías
        numbers = [int(line) for line in lines if line]

        # Si no quedan números, termina
        if not numbers:
            break

        # Encuentra el número mínimo
        min_number = min(numbers)

        # Escribe el número mínimo en el archivo de salida
        output_file.write(str(min_number) + '\n')

        # Encuentra el índice del archivo que contenía el número mínimo
        min_index = numbers.index(min_number)

        # Lee la siguiente línea del archivo correspondiente
        lines[min_index] = file_handles[min_index].readline().strip()

    # Cierra los archivos de entrada
    for file_handle in file_handles:
        file_handle.close()


block1_filename = 'bloque_0.txt'
block2_filename = 'bloque_1.txt'
output_filename = 'resultado.txt'
archivos = ['bloque_0.txt','bloque_1.txt','bloque_2.txt','bloque_3.txt','bloque_4.txt']
tamaño_bloque = 1000000

with open('datos.txt', 'r') as archivo_original:
    lineas = archivo_original.readlines()
    for i in range(0, len(lineas), tamaño_bloque):
        bloque = lineas[i:i + tamaño_bloque]
        ordenamientoRapido(bloque)
        with open(f'bloque_{i // tamaño_bloque}.txt', 'w') as archivo_bloque:
            archivo_bloque.writelines(bloque)

archivos_ordenados = [f'bloque_{i}.txt' for i in range(len(lineas) // tamaño_bloque)]

with open(output_filename, 'w') as output_file:
    merge_blocks(archivos, output_file)