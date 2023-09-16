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
#--------------------------------------------------------------------------------------------------------------------
crear_archivo_de_datos('datos.txt')
#--------------------------------------------------------------------------------------------------------------------
def split_and_store_alternate(archivo, block_size):
    tamaño_archivo = 0
    with open(archivo, 'r') as input_file, open("archivo_1.txt", 'a+') as file1, open("archivo_2.txt", 'a+') as file2:
        block_count = 0  # Contador de bloques

        while True:
            bloque = []
            bloque = [int(input_file.readline().strip()) for _ in range(block_size) if input_file.readline().strip()]

            tamaño_archivo += len(bloque)

            if not bloque:  # Verifica si el bloque está vacío
                break  # Sale del ciclo while si llega al final del archivo
            
            bloque_ordenado = sorted(bloque)

            if block_count % 2 == 0:
                file1.writelines([str(num) + '\n' for num in bloque_ordenado])
            else:
                file2.writelines([str(num) + '\n' for num in bloque_ordenado])

            block_count += 1

    os.remove(archivo)

    with open(archivo, 'a+') as input_file, open("archivo_1.txt", 'r') as file1, open("archivo_2.txt", 'r') as file2:
        line1 = file1.readline().strip()
        line2 = file2.readline().strip()
        while line1 and line2:
            count_archivo_1 = 0
            count_archivo_2 = 0
            while (count_archivo_1 < block_size or count_archivo_2 < block_size) and (line1 and line2):
                
                num1 = int(line1)
                num2 = int(line2)

                # Compara y escribe el número menor en el archivo de salida
                if num1 < num2:
                    input_file.write(str(num1) + '\n')
                    line1 = file1.readline().strip() # Lee la siguiente línea del primer archivo
                    count_archivo_1 += 1
                else:
                    input_file.write(str(num2) + '\n')
                    line2 = file2.readline().strip() # Lee la siguiente línea del segundo archivo
                    count_archivo_2 += 1
            if line1 and line2:
                # Copiar el resto de los números si uno de los bloques se vacía
                while count_archivo_1 <= block_size:
                    input_file.write(line1 + '\n')
                    line1 = file1.readline().strip()
                    count_archivo_1 += 1
                while count_archivo_2 <= block_size:
                    input_file.write(line2 + '\n')
                    line2 = file2.readline().strip()
                    count_archivo_2 += 1
            else:
                break
        while line1:
            input_file.write(line1 + '\n')
            line1 = file1.readline().strip()
        while line2:
            input_file.write(line2 + '\n')
            line2 = file2.readline().strip()

    os.remove("archivo_1.txt")
    os.remove("archivo_2.txt")
    
    block_size *= 2

    if block_size >= tamaño_archivo:
        return
    # Recursividad
    split_and_store_alternate(archivo,block_size)
#--------------------------------------------------------------------------------------------------------------------
def verificar_ordenamiento(nombre):
    claves = []
    with open(nombre, 'r') as archivo:
        claves = [int(linea.strip()) for linea in archivo]
    return claves == sorted(claves) 
#--------------------------------------------------------------------------------------------------------------------
tamaño_de_bloque = 10**6

# Llamada a la función
split_and_store_alternate('datos.txt', tamaño_de_bloque)

print("Ordenado -->", verificar_ordenamiento('datos.txt'))