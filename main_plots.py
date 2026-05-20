import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
plt.plot(x, y)
plt.show()

n1 = [4, 7, 10, 11, 15]
n2 = [1, 9, 12, 17, 19]
plt.scatter(n1, n2, color = "orange")
plt.show()

#Limits number on each axis
plt.plot(n1, n2, color = "purple")
plt.axis([4, 15, 1, 20])
plt.show()

plt.plot(n1, n2, linewidth = 5, label = "line 1", color = "yellow")
plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()

#Plot multiple graphs on a single plot
plt.plot(x, y, linewidth = 5, label = "line 1", color = "green")