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


for i in range(100, 2000, 200):
    pi = montecarlo(i)
    print(i, pi, abs(pi-math.pi))
x=[] 
y=[]
 
for i in range(10, 2000, 10):
    pi = montecarlo(i)
    x.append(i)
    y.append(abs(pi-math.pi))

avg = sum(y)/len(y)
print()
print(avg, avg*100)

plt.plot(x, y)
plt.title('Logarytm błędów obliczenia warości', fontsize=25)
plt.xlabel('n', fontsize=20)
plt.ylabel('błąd', fontsize=20)
plt.grid(True)
plt.savefig('images/mc.png')
plt.show()
