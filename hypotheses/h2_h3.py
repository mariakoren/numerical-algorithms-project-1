import math
import numpy as np
import matplotlib.pyplot as plt

def h2(n):
    teta = 2 * math.pi / n
    w = []
    w.append(np.array([math.cos(teta) - 1, math.sin(teta) + 0]))
    pomoc = np.array([[math.cos(teta), -math.sin(teta)], 
                      [math.sin(teta), math.cos(teta)]])
    for i in range(1, n):
        w.append(pomoc @ w[i-1].transpose())    
    suma_wektorow = np.sum(w, axis=0) 
    return suma_wektorow

x = []
y = []
for i in range(10, 5000, 10):
    sum = h2(i)
    x.append(sum[0])
    y.append(sum[1])
sum_5 = h2(5)
x.append(sum_5[0])
y.append(sum_5[1])




def h3(n):
    teta = 2 * math.pi / n
    w = []
    w.append(np.array([math.cos(teta) - 1, math.sin(teta) + 0]))
    pomoc = np.array([[math.cos(teta), -math.sin(teta)], 
                      [math.sin(teta), math.cos(teta)]])
    for i in range(1, n):
        w.append(pomoc @ w[i-1].transpose())
    return w

def coordinates(w, coord, znak):
    res = []
    for el in w:
        if coord == "x":
            if znak == "+":
                if el[0] > 0:
                    res.append(el[0])
            elif znak =="-":
                if el[0] < 0:
                    res.append(el[0])
        if coord == "y":
            if znak == "+":
                if el[1] > 0:
                    res.append(el[1])
            elif znak =="-":
                if el[1] < 0:
                    res.append(el[1])
    if znak == "+":
        res.sort()
    elif znak =="-":
        res.sort(reverse=True)
    return res

def suma(n):
    w = h3(n)

    xplus = coordinates(w, "x", "+")
    xminus = coordinates(w, "x", "-")
    yplus = coordinates(w, "y", "+")
    yminus = coordinates(w, "y", "-")

    sxplus = 0
    for el in xplus:
        sxplus += el

    sxminus = 0
    for el in xminus:
        sxminus+= el

    syplus = 0
    for el in yplus:
        syplus+= el

    syminus = 0
    for el in yminus:
        syminus+= el

    xcoord = sxplus + sxminus
    ycoord = syplus + syminus
    return xcoord, ycoord


x1 = []
y1 = []
for i in range(10, 5000, 10):
    sum = suma(i)
    x1.append(sum[0])
    y1.append(sum[1])
sum5 = suma(5)
x1.append(sum5[0])
y1.append(sum5[1])

d=[]
for i in range(len(x)):
   d.append( math.sqrt(x[i]**2+y[i]**2) - math.sqrt(x1[i]**2+y1[i]**2) )


def oblicz_procent_liczb(tablica):
    liczba_nieujemnych = 0
    for liczba in tablica:
        if liczba > 0:
            liczba_nieujemnych+=1
    liczba_ujemnych = len(tablica) - liczba_nieujemnych
    procent_nieujemnych = (liczba_nieujemnych / len(tablica)) * 100
    procent_ujemnych = (liczba_ujemnych / len(tablica)) * 100
    return procent_nieujemnych, procent_ujemnych

def rysuj_diagram(procent_nieujemnych, procent_ujemnych):
    etykiety = ['Nieujemne', 'Ujemne']
    wartosci = [procent_nieujemnych, procent_ujemnych]
    kolory = ['lightgreen', 'lightcoral']
    plt.pie(wartosci, labels=etykiety, colors=kolory, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Procent liczb nieujemnych i ujemnych')
    plt.savefig('images/h3.png')
    plt.show()

procent_nieujemnych, procent_ujemnych = oblicz_procent_liczb(d)
rysuj_diagram(procent_nieujemnych, procent_ujemnych)