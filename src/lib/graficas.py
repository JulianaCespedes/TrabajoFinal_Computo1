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
    param = []
    x = []
    y = []

    while row is not None:
        param.append(row[0])
        x.append(row[1])
        y.append(row[2])
        row = db.fetchone()
    return param, x, y

def graficar (data_gen,data_gen2,x2,y2):
    x1 = 0
    y1 = 0
    
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
    plt.suptitle('Prueba')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.xticks(np.arange(0,300+1,30))

    plt.show()

def graficar2(array,name,name2):    
    k = 1
    plt.figure('Graficas.')
    plt.suptitle(u''+name2+' vs posicion')   

    for i in array:
        param,x,y = extraer_dato('SELECT '+name2+', distancia_maxima, altura_maxima FROM resultados\
            WHERE '+name+' = '+str(i)+' AND distancia = 3.0 ')

        plt.subplot(3,2,k)
        plt.plot(param,y, color="blue",linestyle="",marker="o",label=r"Grafica1")
        plt.xticks(np.arange(0,max(param)+1,5))

        plt.xlabel(name2)
        plt.ylabel('y [m]')
        plt.legend([name+'='+str(i)])
        plt.grid()

        plt.subplot(3,2,k+1)
        plt.plot(param,x, color="purple",linestyle="",marker="o",label=r"Grafica1")
        plt.xticks(np.arange(0,max(param)+1,5))

        plt.xlabel(name2)
        plt.ylabel('x [m]')
        plt.legend([name+'='+str(i)])
        plt.grid()

        k = k + 2

    plt.show()