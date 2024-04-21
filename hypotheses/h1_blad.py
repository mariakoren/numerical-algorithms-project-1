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

x = []
y = []
a = []
for i in range(10, 5000, 10):
    pi = calculate_polygon_circumference(i)
    x.append(i)
    y.append(math.log(abs(pi-2*math.pi)))
    a.append(abs(pi-2*math.pi))

avg = sum(a) / len(a) 
print(avg, avg*100)




plt.plot(x, y)
plt.title('Wykres błędów obliczenia', fontsize=20)
plt.xlabel('n', fontsize=14)
plt.ylabel('błąd', fontsize=14)
plt.grid(True)
plt.savefig('images/h1_blad.png')
plt.show()