import os
import globales
import montos_aleatorios
import estadisticas


def menu_principal():
    while True:
        os.system("cls")
        print("MENÚ PRINCIPAL")
        print("")
        print("1. Asignar montos aleatorios")
        print("2. Ver estadísticas")
        print("3. Salir del programa")
        print("")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            os.system("cls")
            montos_aleatorios.generar_montos_aleatorios()
            print("Montos Aleatorios realizados correctamente.")
            input()
        elif opcion == 2:
            os.system("cls")
            print("Resumen estadística:")
            estadisticas.calculo_estadistico()
            input()
        elif opcion == 3:
            os.system("cls")
            print("Saliendo del sistema")
            return
        
if __name__ == "__main__":
    menu_principal()