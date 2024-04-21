import math
import numpy as np
import matplotlib.pyplot as plt
import heapq

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


def h5(n):
    teta = 2 * math.pi / n
    w = []
    w.append(np.array([math.cos(teta) - 1, math.sin(teta) + 0]))
    pomoc = np.array([[math.cos(teta), -math.sin(teta)], 
                      [math.sin(teta), math.cos(teta)]])
    for i in range(1, n):
        w.append(pomoc @ w[i-1].transpose())
    return w

def calculate_sum(vector_list):
    positive_x = []
    negative_x = []
    positive_y = []
    negative_y = []
    
    for vector in vector_list:
        if vector[0] >= 0:
            heapq.heappush(positive_x, vector[0])
        else:
            heapq.heappush(negative_x, vector[0])
        
        if vector[1] >= 0:
            heapq.heappush(positive_y, vector[1])
        else:
            heapq.heappush(negative_y, vector[1])
    
    sum_positive_x = 0
    while len(positive_x) > 1:
        min_value1 = heapq.heappop(positive_x)
        min_value2 = heapq.heappop(positive_x)
        sum_value = min_value1 + min_value2
        heapq.heappush(positive_x, sum_value)
    if positive_x:
        sum_positive_x += positive_x[0]
    sum_negative_x = 0
    while len(negative_x) > 1:
        min_value1 = heapq.heappop(negative_x)
        min_value2 = heapq.heappop(negative_x)
        sum_value = min_value1 + min_value2
        heapq.heappush(negative_x, sum_value)
    if negative_x:
        sum_negative_x += negative_x[0]
    sum_positive_y = 0
    while len(positive_y) > 1:
        min_value1 = heapq.heappop(positive_y)
        min_value2 = heapq.heappop(positive_y)
        sum_value = min_value1 + min_value2
        heapq.heappush(positive_y, sum_value)
    if positive_y:
        sum_positive_y += positive_y[0]
    sum_negative_y = 0
    while len(negative_y) > 1:
        min_value1 = heapq.heappop(negative_y)
        min_value2 = heapq.heappop(negative_y)
        sum_value = min_value1 + min_value2
        heapq.heappush(negative_y, sum_value)
    if negative_y:
        sum_negative_y += negative_y[0]
    
    return sum_positive_x, sum_negative_x, sum_positive_y, sum_negative_y



x2 = []
y2 = []
vectors = h5(5)
sum_x_positive, sum_x_negative, sum_y_positive, sum_y_negative = calculate_sum(vectors)
x2.append(sum_x_positive+sum_x_negative)
y2.append(sum_y_positive+sum_y_negative)


for i in range(10, 5000, 10):
    vectors = h5(i)
    sum_x_positive, sum_x_negative, sum_y_positive, sum_y_negative = calculate_sum(vectors)
    x2.append(sum_x_positive+sum_x_negative)
    y2.append(sum_y_positive+sum_y_negative)


d=[]
for i in range(len(x1)):
   d.append( math.sqrt(x1[i]**2+y1[i]**2) - math.sqrt(x2[i]**2+y2[i]**2) )


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
    plt.savefig('images/h3h5.png')
    plt.show()

procent_nieujemnych, procent_ujemnych = oblicz_procent_liczb(d)
rysuj_diagram(procent_nieujemnych, procent_ujemnych)