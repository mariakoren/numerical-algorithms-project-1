#tabela 1
import math
import numpy as np
import matplotlib.pyplot as plt

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

x= []
y =[]
for i in range(10, 200, 20):
    pi = calculate_polygon_circumference(i)
    x.append(i)
    y.append(pi)
    print(i, pi, abs(pi-2*math.pi))

for i in range(200, 1200, 200):
    pi = calculate_polygon_circumference(i)
    x.append(i)
    y.append(pi)
    print(i, pi, abs(pi-2*math.pi))

