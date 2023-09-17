from random import randint
import os
#--------------------------------------------------------------------------------------------------------------------
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
def ordenamiento_externo(archivo, block_size):
    # Contador para el tamaño total del archivo original
    tam_archivo = 0
    with open(archivo, 'r') as input_file, open("archivo_1.txt", 'a+') as file1, open("archivo_2.txt", 'a+') as file2:
        block_count = 0  # Contador de bloques
        while True:  
            bloque = []

            # Lee líneas del archivo de entrada para crear un bloque
            for _ in range(block_size):
                linea1 = input_file.readline().strip()           
                if not linea1:  # Verifica si la línea está vacía (fin del archivo)
                    break  # Sale del ciclo for si llegaste al final del archivo
                bloque.append(int(linea1))
                tam_archivo += 1

            if not bloque:  # Si el bloque está vacío, significa que llegaste al final del archivo
                break  # Sale del ciclo while si llegaste al final del archivo

            # Ordena el bloque
            bloque.sort()

            # Escribe el bloque ordenado en el archivo temporal correspondiente
            if block_count % 2 == 0:
                for num in bloque:
                    file1.write(str(num) + '\n')
            else:
                for num in bloque:
                    file2.write(str(num) + '\n')
            block_count += 1

    # Elimina el archivo original
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
            # Verifica que no esté al final
            if line1 and line2:
                # Copia el resto de los números si uno de los bloques se vacía
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

        # Copia las líneas restantes de file1 y file2 al archivo de entrada
        while line1:
            input_file.write(line1 + '\n')
            line1 = file1.readline().strip()
        while line2:
            input_file.write(line2 + '\n')
            line2 = file2.readline().strip()
    # Elimina los archivos temporales
    os.remove("archivo_1.txt")
    os.remove("archivo_2.txt")

    block_size *= 2

    # Llamada recursiva si el tamaño del bloque es menor que el tamaño total del archivo
    if block_size < tam_archivo:
        ordenamiento_externo(archivo,block_size)
    else:
        return
#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------
def verificar_ordenamiento(nombre):
    datos_arch = []
    with open(nombre, 'r') as archivo:
        datos_arch = [int(linea.strip()) for linea in archivo]
    return datos_arch == sorted(datos_arch)
#--------------------------------------------------------------------------------------------------------------------
tamaño_de_bloque = 10**6

ruta_al_archivo = "datos.txt"

tamaño_original_kb = os.path.getsize(ruta_al_archivo) / 1024

# print(f"El tamaño del archivo {ruta_al_archivo} antes de aplicar el ordenamiento es de {tamaño_original_kb} KB")

ordenamiento_externo('datos.txt', tamaño_de_bloque)

tamaño_ordenado_kb = os.path.getsize(ruta_al_archivo) / 1024

print("Comparación de tamaño del archivo original con el ordenado --->", tamaño_original_kb == tamaño_ordenado_kb)
print("Verificamos que esté ordenado --> ", verificar_ordenamiento('datos.txt'))


