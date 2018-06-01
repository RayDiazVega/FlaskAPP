import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
style.use('ggplot')
import numpy as np
import sympy as sy
Writer = animation.writers['ffmpeg']
writer = Writer(fps=4, metadata=dict(artist='Me'), bitrate=18000)

class Newton(object):
    """docstring for Newton"""
    def __init__(self, ecuacion = "(x-2)**3+4", x_inicial = 5, grado = 6):
        def metodo(self, frm, tabla, fig, ax, x, f, df, tangent_line, sdf):
            x_p = self.x_initial
            err = 1
            i = 0
            while err > self.tol:
                im1 = ax.plot(x, f(x))
                im2 = ax.axhline(color='black')  
                im3 = ax.axvline(color='black') 
                im4 = ax.plot(x_p, 0, marker='o')
                im5 = ax.text(0.5, 1, 'Iteracion '+str(i)+", x = "+str(x_p), ha='center', va='bottom', transform=ax.transAxes)
                frm.append(im1 + [im2] + [im3] + im4 + [im5])
                
                im6 = ax.plot(x_p, f(x_p), marker='o')
                frm.append(im1 + [im2] + [im3] + im4 + [im5] + im6)

                im7 = ax.plot(x, tangent_line(x, x_p), 'b--')
                im8 = ax.plot(x_p, f(x_p), marker='o')
                frm.append(im1 + [im2] + [im3] + im4 + [im5]+ im6 + im7 + im8)

                x_x = x_p - f(x_p)/df(x_p)
                im9 = ax.plot(x_x, 0, marker='o')
                frm.append(im1 + [im2] + [im3] + im4 + [im5]+ im6 + im7 + im8 + im9)

                err = abs(x_x - x_p)/abs(x_x)
                tabla.append([i,x_p,f(x_p),df(x_p),err])
                x_p = x_x
                i += 1
            x = sy.symbols('x')
            m = ["Solucion convergente: "+str(x_x),"Numero de iteraciones: "+str(i-1),"Tolerancia: "+str(self.tol),"Valor inicial: "+str(self.x_initial),"Solucion analitica: "+str((sy.solve(f(x), x)[0]))]
            ani = animation.ArtistAnimation(fig, frm, interval=1000, blit=True)
            ani.save('static/video/Grafica1.mp4', writer = writer)
            plt.show()
            return x_x, i, tabla, m, sdf

        def calculo(self):

            def f(x):
                return eval(self.ecuacion)

            def tangent_line(x, x_i):
                return df(x_i) * (x - x_i) + f(x_i)

            sy.init_printing(use_unicode=True)
            x = sy.symbols('x')
            sdf = df = sy.diff(f(x), x)
            df = sy.lambdify(x, df)

            xlim, ylim = -self.x_initial, self.x_initial
            frm=[]
            tabla = []
            fig, ax = plt.subplots()
            x = np.linspace(xlim, ylim)
            im1 = ax.plot(x, f(x))
            im2 = ax.axhline(color='black')
            im3 = ax.axvline(color='black')
            frm.append(im1 + [im2] + [im3])
            plt.ylabel('Eje Y')
            plt.xlabel('Eje X')
            plt.suptitle("f(x)="+self.ecuacion)
            return metodo(self, frm, tabla, fig, ax, x, f, df, tangent_line, sdf)

        self.ecuacion = str(ecuacion)
        self.x_initial = float(x_inicial)
        self.tol = 10.0**(-abs(int(grado)))
        self.sol, self.iter, self.tabla, self.men, self.df= calculo(self)
    def resultado(self):
        return self.tabla, self.men, self.df

class Punto(object):
    """docstring for Newton"""
    def __init__(self, ecuacion = "(10/(x+4))**0.5", x_inicial = 1.5, grado = 7):
        def metodo(self, frm, tabla, fig, ax, x, f):
            x_p = self.x_initial
            err = 1
            i = 0
            while err > self.tol:
                im1 = ax.plot(x, f(x))
                im2 = ax.axhline(color='black')  
                im3 = ax.axvline(color='black') 
                im4 = ax.plot(x_p, 0, marker='o')
                im5 = ax.text(0.5, 1, 'Iteracion '+str(i)+", x = "+str(x_p), ha='center', va='bottom', transform=ax.transAxes)
                frm.append(im1 + [im2] + [im3] + im4 + [im5])
                
                im6 = ax.plot(x_p, f(x_p), marker='o')
                frm.append(im1 + [im2] + [im3] + im4 + [im5] + im6)

                
                im7 = ax.plot(x_p, f(x_p), marker='o')
                frm.append(im1 + [im2] + [im3] + im4 + [im5] + im6 + im7)

                x_x = f(x_p)
                im8 = ax.plot([x_p], [f(x_x)], 'b--')
                im9 = ax.plot(x_x, 0, marker='o')
                frm.append(im1 + [im2] + [im3] + im4 + [im5] + im6 + im7 + im8 + im9)

                err = abs(x_x - x_p)/abs(x_x)
                tabla.append([i,x_p,err])
                x_p = x_x
                i += 1
            x = sy.symbols('x')
            m = ["Solucion convergente: "+str(x_x),"Numero de iteraciones: "+str(i-1),"Tolerancia: "+str(self.tol),"Valor inicial: "+str(self.x_initial)]
            ani = animation.ArtistAnimation(fig, frm, interval=1000, blit=True)
            ani.save('static/video/Grafica2.mp4', writer = writer)
            plt.show()
            return x_x, i, tabla, m

        def calculo(self):

            def f(x):
                return eval(self.ecuacion)

            sy.init_printing(use_unicode=True)
            x = sy.symbols('x')

            xlim, ylim = -self.x_initial, self.x_initial
            frm=[]
            tabla = []
            fig, ax = plt.subplots()
            x = np.linspace(xlim, ylim)
            im1 = ax.plot(x, f(x))
            im2 = ax.axhline(color='black')
            im3 = ax.axvline(color='black')
            frm.append(im1 + [im2] + [im3])
            plt.ylabel('Eje Y')
            plt.xlabel('Eje X')
            plt.suptitle("f(x)="+self.ecuacion)
            return metodo(self, frm, tabla, fig, ax, x, f)

        self.ecuacion = str(ecuacion)
        self.x_initial = float(x_inicial)
        self.tol = 10.0**(-abs(int(grado)))
        self.sol, self.iter, self.tabla, self.men = calculo(self)
    def resultado(self):
        return self.tabla, self.men

class Euler(object):
    """docstring for Newton"""
    def __init__(self, ecuacion = "9.81-(0.04736*y)", x_inicial = 0.0, a = 0.0, b = 5.0, intervalo = 10):
        def metodo(self, frm, tabla, fig, ax, f):
            i = 0.0
            t = self.a
            y = self.x_initial
            while i <= self.intervalo and t <= self.b:
                im1 = ax.axhline(color='black')
                im2 = ax.axvline(color='black') 
                im3 = ax.plot(y, 0, marker='o')
                im4 = ax.text(0.5, 1, 'Iteracion '+str(i)+", W = "+str(y), ha='center', va='bottom', transform=ax.transAxes)
                frm.append([im1] + [im2] + im3 + [im4])
                
                im5 = ax.plot(t, y, f(y,t), marker='o')
                frm.append([im1] + [im2] + im3 + [im4] + im5)
                
                tabla.append([i,t,y])
                i += 1.0
                t = self.a + self.h*i
                y = y + self.h*f(y,t)
                
            m = ["Solucion convergente: "+str(y),"Numero de iteraciones: "+str(i-1),"Valor inicial: "+str(self.x_initial)]
            ani = animation.ArtistAnimation(fig, frm, interval=1000, blit=True)
            ani.save('static/video/Grafica3.mp4', writer = writer)
            plt.show()
            return y, tabla, m

        def calculo(self):

            def f(y,t):
                return eval(self.ecuacion)

            sy.init_printing(use_unicode=True)
            xlim, ylim = self.a, self.b
            frm = []
            tabla = []
            fig, ax = plt.subplots()
            im1 = ax.axhline(color='black')
            im2 = ax.axvline(color='black')
            frm.append([im1] + [im2])
            plt.ylabel('Eje y')
            plt.xlabel('Eje t')
            plt.suptitle("W_x+1 = "+str(self.x_initial)+str(self.h)+"("+self.ecuacion+")")
            return metodo(self, frm, tabla, fig, ax, f)

        self.ecuacion = str(ecuacion)
        self.x_initial = float(x_inicial)
        self.a = float(a)
        self.b = float(b)
        self.intervalo = float(intervalo)
        self.h = (b - a)/intervalo
        self.sol, self.tabla, self.men = calculo(self)
    def resultado(self):
        return self.tabla, self.men

class Taylor(object):
    """docstring for Newton"""
    def __init__(self, ecuacion = "9.81-(0.04736*y)", x_inicial = 0.0, a = 0.0, b = 5.0, intervalo = 10):
        def metodo(self, frm, tabla, fig, ax, f):
            i = 0.0
            t = self.a
            y = self.x_initial
            while i <= self.intervalo and t <= self.b:
                im1 = ax.axhline(color='black')
                im2 = ax.axvline(color='black') 
                im3 = ax.plot(y, 0, marker='o')
                im4 = ax.text(0.5, 1, 'Iteracion '+str(i)+", W = "+str(y), ha='center', va='bottom', transform=ax.transAxes)
                frm.append([im1] + [im2] + im3 + [im4])
                
                im5 = ax.plot(t, y, f(y,t), marker='o')
                frm.append([im1] + [im2] + im3 + [im4] + im5)
                
                tabla.append([i,t,f(y,t)])
                i += 1.0
                t = self.a + self.h*i
                y = f(y,t)
                
            m = ["Solucion convergente: "+str(y),"Numero de iteraciones: "+str(i-1),"Valor inicial: "+str(self.x_initial)]
            ani = animation.ArtistAnimation(fig, frm, interval=1000, blit=True)
            ani.save('static/video/Grafica4.mp4', writer = writer)
            plt.show()
            return y, tabla, m

        def calculo(self):

            def f(y,t):
                return eval(self.ecuacion)

            sy.init_printing(use_unicode=True)
            x = sy.symbols('x')
            sdf = df = sy.diff(f(x), x)
            df = sy.lambdify(x, df)

            xlim, ylim = self.a, self.b
            frm = []
            tabla = []
            fig, ax = plt.subplots()
            im1 = ax.axhline(color='black')
            im2 = ax.axvline(color='black')
            frm.append([im1] + [im2])
            plt.ylabel('Eje y')
            plt.xlabel('Eje t')
            plt.suptitle("W_x+1 = "+str(self.x_inicial)+str(self.h)+"("+self.ecuacion+")")
            return metodo(self, frm, tabla, fig, ax, f)

        self.ecuacion = str(ecuacion)
        self.x_initial = float(x_inicial)
        self.a = float(a)
        self.b = float(b)
        self.intervalo = float(intervalo)
        self.h = (b - a)/intervalo
        self.sol, self.tabla, self.men = calculo(self)
    def resultado(self):
        return self.tabla, self.men