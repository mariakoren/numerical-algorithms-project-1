import heapq
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


x = []
y = []
vectors = calculate_polygon_circumference(5)
sum_x_positive, sum_x_negative, sum_y_positive, sum_y_negative = calculate_sum(vectors)
print(5, sum_x_positive+sum_x_negative, sum_y_positive + sum_y_negative)
x.append(sum_x_positive+sum_x_negative)
y.append(sum_y_positive+sum_y_negative)

for i in range(10, 200, 10):
    vectors = calculate_polygon_circumference(i)
    sum_x_positive, sum_x_negative, sum_y_positive, sum_y_negative = calculate_sum(vectors)
    print(i, sum_x_positive+sum_x_negative, sum_y_positive + sum_y_negative)

for i in range(200, 1200, 200):
    vectors = calculate_polygon_circumference(i)
    sum_x_positive, sum_x_negative, sum_y_positive, sum_y_negative = calculate_sum(vectors)
    print(i, sum_x_positive+sum_x_negative, sum_y_positive + sum_y_negative)




for i in range(10, 5000, 10):
    vectors = calculate_polygon_circumference(i)
    sum_x_positive, sum_x_negative, sum_y_positive, sum_y_negative = calculate_sum(vectors)
    x.append(sum_x_positive+sum_x_negative)
    y.append(sum_y_positive+sum_y_negative)

plt.scatter(x, y, marker = "o")
plt.title('Wykres wartości sumy wektorów', fontsize=25)
plt.xlabel('x', fontsize=20)
plt.ylabel('y', fontsize=20)
plt.grid(True)
plt.savefig('images/heap.png')
plt.show()