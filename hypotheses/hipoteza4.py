from random import random
import numpy as np
import matplotlib.pyplot as plt
import math

def montecarlo(n):
    coordinates = []
    a=0
    for i in range(n):
        x = random()
        y = random()
        d = x**2+y**2
        if d <= 1:
            a += 1
        coordinates.append({"x": x, "y": y})
    pi = 4*a/n
    return pi

    pi = montecarlo(i)

x=[] 
y=[]
for i in range(10, 5000, 10):
    pi = montecarlo(i)
    x.append(i)
    y.append(math.log(abs(pi-math.pi)))




def calculate_polygon_circumference(n):
    teta = 2 * math.pi / n
    w = []
    w.append(np.array([math.cos(teta) - 1, math.sin(teta) + 0]))
    length = math.sqrt(w[0][0]**2+w[0][1]**2)
    pomoc = np.array([[math.cos(teta), -math.sin(teta)], 
                      [math.sin(teta), math.cos(teta)]])
    for i in range(1, n):
        w.append(pomoc @ w[i-1].transpose())
        length += math.sqrt(w[i][0]**2+w[i][1]**2)
    return length

x1 = []
y1 =[]
for i in range(10, 5000, 10):
    pi = calculate_polygon_circumference(i)/2
    x1.append(i)
    y1.append(math.log(abs(pi-math.pi)))


plt.plot(x, y, label='Monte Carlo') 
plt.plot(x1, y1, label='Sumowanie wektorów', color='purple')
plt.title('Wykres błędów obliczenia', fontsize=25)
plt.xlabel('n', fontsize=20)
plt.ylabel('błąd', fontsize=20)
plt.grid(True)
plt.legend()
plt.savefig('images/h4.png')
plt.show()
