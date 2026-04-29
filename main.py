import matplotlib.pyplot as plt
import numpy as np

#histogram
ages = [10, 17, 21, 29, 31, 36, 45, 56, 63]
bins = [10, 20, 30, 40, 50, 60]
plt.hist(ages, bins, edgecolor = "black", color = "red")
plt.title("Frequency of Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#pie chart
sections = [25, 15, 37, 11, 12]
activities = ["Sports", "Videogames", "TV", "Studying", "Eating"]
colors = ["blue", "red", "green", "yellow", "purple"]
plt.pie(sections, labels = activities, colors = colors, startangle = 90, autopct = '%1.1f%%')
plt.title("Pie Chart of Activities")
plt.axis("equal")
plt.show()

#scatter plot
x = ["school", "library", "hospital", "cafe", "shop"]
y = [5, 4, 6, 3, 7]
plt.scatter(x, y, color = "blue")
plt.title("Scatter Plot")
plt.xlabel("Places")
plt.ylabel("Frequencies")
plt.show()

#stackplot
days = [1, 2, 3, 4, 5]
sports = [3, 2, 1, 2, 3]
sightseeing = [5, 4, 6, 4, 3]
cooking = [2, 3, 1, 4, 3]
plt.stackplot(days, sports, sightseeing, cooking, labels = ["Sports, Sightseeing, Cooking"], colors = ["red", "green", "cyan"])
plt.title("Daily Activities Over Time")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.legend(loc = "upper left")
plt.show()