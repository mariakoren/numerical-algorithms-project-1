import numpy as np
import matplotlib.pyplot as plt
import math

def calculate_polygon_circumference(n):
    teta = 2 * math.pi / n
    w = []
    w.append(np.array([math.cos(teta) - 1, math.sin(teta) + 0]))
    length = math.sqrt(w[0][0]**2 + w[0][1]**2)
    pomoc = np.array([[math.cos(teta), -math.sin(teta)], 
                      [math.sin(teta), math.cos(teta)]])
    for i in range(1, n):
        w.append(np.dot(pomoc, w[i-1].transpose()))
        length += math.sqrt(w[i][0]**2 + w[i][1]**2)
    return length

# Parametry testu
n_values = np.arange(3, 101) 
num_tests = 1000 

method_errors = []
roundoff_errors = []

for n in n_values:
    circumferences = np.array([calculate_polygon_circumference(n) for _ in range(num_tests)])
    exact_circumference = 2 * np.pi
    method_error = np.abs(circumferences - exact_circumference)
    roundoff_error = np.finfo(float).eps * np.abs(exact_circumference)
    
    method_errors.append(np.mean(method_error))
    roundoff_errors.append(roundoff_error)

# Tworzenie wykresu
plt.figure(figsize=(10, 6))

plt.plot(n_values, method_errors, label='Błąd metody')
plt.plot(n_values, roundoff_errors, label='Błąd zaokrąglenia')

plt.xlabel('Liczba wierzchołków wielokąta (n)')
plt.ylabel('Błąd')
plt.title('Błąd metody vs. Błąd zaokrąglenia w obliczaniu obwodu wielokąta')
plt.legend()
plt.grid(True)

plt.show()
