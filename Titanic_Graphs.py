import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv("Titanic-Dataset.csv")

#bar graph for total number of men and women passengers on the Titanic
gender_count = data["Sex"].value_counts()
plt.bar(gender_count.index, gender_count.values, color = "orange")
plt.xlabel("Gender")
plt.ylabel("Counts")
plt.title("Total Number of Men and Women")
plt.show()

#bar graph for the average fare of men and women in the Titanic
avg_fare = data.groupby("Sex")["Fare"].mean()
plt.bar(avg_fare.index, avg_fare.values, color = "red")
plt.xlabel("Gender")
plt.ylabel("Average Fare")
plt.title("Average Fare of Men and Women")
plt.show()