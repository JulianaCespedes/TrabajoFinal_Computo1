import math
import numpy as np
import sqlite3 as sq
import matplotlib.pyplot as plt
from .database import Database
db = Database('Resultados.db')

def condiciones_iniciales():
    v0 = []
    x0 = []
    θ = []

    for i in range (0,10):
        i = i + 1
        v = i * 5
        d = i * 3
        v0.append(v)
        x0.append(d)
    for l in range (0,90):
        l = l + 1
        a = math.radians(l)
        θ.append(a)
    return v0, x0, θ

def generar_datos(v0,x0,θ):
    g = 9.8

    for i in v0:
        for j in x0:
            for k in θ:
                v0x = (i * (math.cos(k)))
                v0y = (math.sqrt ((i ** 2) - (v0x ** 2)))
                t = np.amax(np.roots([-5,v0y,10]))
                x = ((v0x * t) + j)
                vfy = (v0y + (g * t))
                ymax = ((10 + (v0y ** 2 ) / g) - ((v0y ** 2) / (2 * g)))
                vf = (math.sqrt ((v0x ** 2) + (vfy ** 2)))

                a = round(math.degrees(k))
                ab = float(("%.4f"%vf))
                ac = float(("%.4f"%t))
                ad = float(("%.4f"%x))
                ae = float(("%.4f"%ymax))

                db.execute("INSERT INTO resultados (velocidad, distancia, angulo, velocidad_final, tiempo_total, distancia_maxima, altura_maxima) \
                    VALUES (?,?,?,?,?,?,?)",(i,j,a,ab,ac,ad,ae))
                db.commit()

def create_data():
    db.execute(' CREATE TABLE IF NOT EXISTS resultados (velocidad, distancia, angulo, velocidad_final, tiempo_total, distancia_maxima, altura_maxima)')
    db.commit()
    db.execute('SELECT COUNT(*) FROM resultados')
    row = db.fetchone()
    if row[0] < 9000:
        db.execute('DELETE FROM resultados')
        v0,x0,θ = condiciones_iniciales()
        generar_datos(v0,x0,θ)
