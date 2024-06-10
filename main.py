import sys
sys.path.append(r'C:\Users\Ramiro\Desktop\pYTHON')
from Package_operaciones import *
from lista_peliculas import peliculas
from peliculas import *
import os

bandera_permitir = False

while True:
    os.system('cls')  # Limpiar la consola en Windows, cambiar a 'clear' para sistemas Unix/Linux
    opcion = get_int("""Seleccione una opción.\n
                     1. Dar de alta.\n
                     2. Modificar.\n
                     3. Eliminar\n
                     4. Mostrar películas.\n
                     5. Ordenar películas.\n
                     6. Buscar películas.\n
                     7. Calcular\n
                     8. Calcular porcentaje.\n
                     9. Salir\n""", "Error seleccione una opcion valida", 1, 9)

    match opcion:
        case 1:
            agregar_pelicula(peliculas)
            bandera_permitir = True
        case 2:
            if bandera_permitir:
                modificar_pelicula(peliculas)
            else:
                print("Debe haber dado de alta al menos una película.")
        case 3:
            if bandera_permitir:
                eliminar_pelicula(peliculas)
            else:
                print("Debe haber dado de alta al menos una película.")
        case 4:
            if bandera_permitir:
                mostrar_peliculas(peliculas)
            else:
                print("Debe haber dado de alta al menos una película.")
        case 5:
            if bandera_permitir:
                ordenar_peliculas(peliculas)
            else:
                print("Debe haber dado de alta al menos una película.")
        case 6:
            if bandera_permitir:
                buscar_pelicula(peliculas)
            else:
                print("Debe haber dado de alta al menos una película.")
        case 7:
            if bandera_permitir:
                calcular_peliculas(peliculas)
            else:
                print("Debe haber dado de alta al menos una película.")
        case 8:
            if bandera_permitir:
                porcentaje_peliculas(peliculas)
            else:
                print("Debe haber dado de alta al menos una película.")
        case 9:
            print("Gracias por usar nuestro programa!")
            break