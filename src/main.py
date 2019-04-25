import math
import numpy as np

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
        graficar()
    elif i == 2:
        graficar2([30,45,90],'angulo','velocidad')
    elif i == 3:
        graficar2([5,25,50],'velocidad','angulo')
    elif i == 4:
        print('Hasta luego.')
    else:
        print('Ha seleccionado un valor incorrecto, intente otra vez.')