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
x1 = [3, 5, 6, 14, 18]
y1 = [7, 8, 10, 16, 21]
plt.plot(x, y, linewidth = 5, label  = "line 1", color = "purple")
plt.plot(x1, y1, linewidth = 5, label = "line 2", color = "red")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Lines Plot")
plt.legend()
plt.show()

#Polynomial functions plot
x = np.arange(0, 10, 0.2)
print(x)
y1 = x**2
y2 = x**3
plt.plot(x, y1, linewidth = 7, label = "line 1", color = "blue")
plt.plot(x, y2, linewidth = 7, label = "line 2", color = "pink")
plt.title("Polynomial Functions")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()

#Plot bar graph
subjects = ["Maths", "Physics", "Spanish", "Geography", "Computer"]
time = [120, 90, 90, 60, 90]
plt.bar(subjects, time, color = "green")
plt.xlabel("Subject")
plt.ylabel("Time")
plt.title("Bar Graph")
plt.show()