import numpy as np

def data_gen(x=0):
    contador = 0
    while contador < 102:
        contador += 1
        yield 30 + ((25 * np.sin(0.785398)) * (4.0316/100)* contador), (10 + ((25 * np.cos(0.785398)) * (4.0316/100)* contador)) - ((9.8 * ((4.0316/100)* contador) ** 2) / 2)
def data_gen2(x=0):
    contador = 0
    while contador < 102:
        contador += 1
        yield 30 + ((50 * np.sin(0.785398)) * (7.3434/100)* contador), (10 + ((50 * np.cos(0.785398)) * (7.3434/100)* contador)) - ((9.8 * ((7.3434/100)* contador) ** 2) / 2)
def data_gen3 (x=0):
    contador = 0
    while contador < 40:
        contador += 1
        yield 21 + ((30 * np.sin(1.16937)) * (5.8641/100)* contador), (10 + ((5 * np.cos(0.785398)) * (5.8641/100)* contador)) - ((9.8 * ((5.8641/100)* contador) ** 2) / 2)
def data_gen4 (x=0):
    contador = 0
    while contador < 16:
        contador += 1
        yield 21 + ((45 * np.sin(1.5708)) * (9.217/100)* contador), (10 + ((5 * np.cos(1.5708)) * (9.217/100)* contador)) - ((9.8 * ((9.217/100)* contador) ** 2) / 2)
def data_gen5 (x=0):
    contador = 0
    while contador < 102:
        contador += 1
        yield 15 + ((15 * np.sin(0.383972)) * (2.0837/100)* contador), (10 + ((5 * np.cos(0.383972)) * (2.0837/100)* contador)) - ((9.8 * ((2.0837/100)* contador) ** 2) / 2)
def data_gen6 (x=0):
    contador = 0
    while contador < 102:
        contador += 1
        yield 15 + ((35 * np.sin(0.383972)) * (3.2396/100)* contador), (10 + ((5 * np.cos(0.383972)) * (3.2396/100)* contador)) - ((9.8 * ((3.2396/100)* contador) ** 2) / 2)
def data_gen7 (x=0):
    contador = 0
    while contador < 80:
        contador += 1
        yield 6 + ((5 * np.sin(1.5708)) * (2.0/100)* contador), (10 + ((5 * np.cos(1.5708)) * (2.0/100)* contador)) - ((9.8 * ((2.0/100)* contador) ** 2) / 2)
def data_gen8 (x=0):
    contador = 0
    while contador < 200:
        contador += 1
        yield 6 + ((5 * np.sin(0.0872665)) * (1.4585/100)* contador), (10 + ((5 * np.cos(0.0872665)) * (1.4585/100)* contador)) - ((9.8 * ((1.4585/100)* contador) ** 2) / 2)