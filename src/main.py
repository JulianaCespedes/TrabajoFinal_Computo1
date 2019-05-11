from lib.funciones import *
from lib.mparab import create_data
from lib.graficas import graficar, graficar2
create_data()

print("Seleccione la opción a la cual desee acceder.\n")
print("1. Muestra graficas animadas. ")
print("2. Muestra graficas de velocidad vs posición. ")
print("3. Muestra graficas de angulo vs posición. ")
print("4. Salir. ")

i = 5

while i != 4:
    i = int(input())
    if i == 1:
        graficar(data_gen,data_gen2,300,100)
        graficar(data_gen3,data_gen4,90,20)
        graficar(data_gen5,data_gen6,60,15)
        graficar(data_gen7,data_gen8,25,15)
    elif i == 2:
        graficar2([30,45,90],'angulo','velocidad')
    elif i == 3:
        graficar2([5,25,50],'velocidad','angulo')
    elif i == 4:
        print('Hasta luego.')
    else:
        print('Ha seleccionado un valor incorrecto, intente otra vez.')