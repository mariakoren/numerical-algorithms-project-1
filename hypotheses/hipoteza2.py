import math
import numpy as np
import matplotlib.pyplot as plt

def calculate_polygon_circumference(n):
    teta = 2 * math.pi / n
    w = []
    w.append(np.array([math.cos(teta) - 1, math.sin(teta) + 0]))
    pomoc = np.array([[math.cos(teta), -math.sin(teta)], 
                      [math.sin(teta), math.cos(teta)]])
    for i in range(1, n):
        w.append(pomoc @ w[i-1].transpose())    
    suma_wektorow = np.sum(w, axis=0)
    return suma_wektorow


sum = calculate_polygon_circumference(5)
print(5, sum)

for i in range(10, 200, 20):
    sum = calculate_polygon_circumference(i)
    print(i, sum)

for i in range(200, 1200, 200):
    sum = calculate_polygon_circumference(i)
    print(i, sum)

x = []
y = []
for i in range(10, 1000, 10):
    sum = calculate_polygon_circumference(i)
    x.append(sum[0])
    y.append(sum[1])

plt.scatter(x, y)
plt.title('Wykres wartości sumy wektorów', fontsize=25)
plt.xlabel('n', fontsize=20)
plt.ylabel('suma', fontsize=20)
plt.grid(True)
plt.tight_layout()
plt.savefig('images/h2.png')
plt.show()