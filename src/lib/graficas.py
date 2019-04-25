import math as m
import numpy as np
import sqlite3 as sq
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .database import Database
db = Database('Resultados.db')

def extraer_dato(query):
    db.execute(query)
    row = db.fetchone()
    vel = []
    x = []
    y = []

    while row is not None:
        vel.append(row[0])
        x.append(row[1])
        y.append(row[2])
        row = db.fetchone()
    return vel, x, y

def graficar ():
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

    x1 = 0
    x2 = 300
    y1 = 0
    y2 = 200

    def init(xmin=x1,xmax=x2,ymin=y1,ymax=y2):
        ax.set_ylim(ymin,ymax)
        ax.set_xlim(xmin,xmax)
        del xdata[:]
        del ydata[:]
        line.set_data(xdata, ydata)
        return line,

    fig3, ax = plt.subplots()
    line, = ax.plot([], [],'b', lw=2)
    line2, = ax.plot([], [],'r', lw=2)
    ax.grid()
    xdata, ydata = [], []

    def run(data):
        t, y = data
        xdata.append(t)
        ydata.append(y)
        xmin, xmax = ax.get_xlim()
        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()
        line.set_data(xdata, ydata)
        return line,
    xdata2, ydata2 = [], []
    def run2(data):
        t, y = data
        xdata2.append(t)
        ydata2.append(y)
        xmin, xmax = ax.get_xlim()
        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()
        line2.set_data(xdata2, ydata2)
        return line2,

    an = animation.FuncAnimation(fig3, run, data_gen, blit=False, interval=100,
                                repeat=False, init_func=init)
    an2 = animation.FuncAnimation(fig3, run2, data_gen2, blit=False, interval=100,
                                repeat=False, init_func=init)
    plt.suptitle('Prueba 1')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.xticks(np.arange(0,300+1,30))

    plt.show()

def graficar2(array,name,name2):    
    k = 1

    for i in array:
        param,x,y = extraer_dato('SELECT '+name2+', distancia_maxima, altura_maxima FROM resultados\
            WHERE '+name+' = '+str(i)+' AND distancia = 3.0 ')

        plt.figure('Figure 2')
        plt.suptitle(u''+name2+' vs Posición')

        plt.subplot(3,2,k)
        plt.plot(param,y, color="blue",linestyle="",marker="o",label=r"Grafica1")
        plt.xticks(np.arange(0,max(param)+1,5))

        plt.xlabel(name2)
        plt.ylabel('y [m]')
        plt.grid()

        plt.subplot(3,2,k+1)
        plt.plot(param,x, color="purple",linestyle="",marker="o",label=r"Grafica1")
        plt.xticks(np.arange(0,max(param)+1,5))

        plt.xlabel(name2)
        plt.ylabel('x [m]')
        plt.grid()

        k = k + 2

    plt.show()