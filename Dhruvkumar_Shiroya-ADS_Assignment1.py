
"""
Created on Mon Nov  7 12:13:56 2022

@author: ds22abr
"""


# Import the library
import pandas as pd
import matplotlib.pyplot as plt



"""
LINE PLT
"""

# Read dataset in file in csv format
energy = pd.read_csv('chicago_energy_benchmarking.csv') 
print(energy)

# Plotting multiple lines graph
plt.figure(figsize=(7,7))
plt.plot(energy["Electricity Use (kBtu)"], label="Electricity Use")
plt.plot(energy["Natural Gas Use (kBtu)"], label="Natural Gas Use")
plt.legend()

# Adding the labels of X and Y 
plt.xlabel("Data")
plt.ylabel("Total Emissions")
plt.show()



"""
PIE PLT
"""

# Read dataset in file in csv format
cal = pd.read_csv('Nutrition_of_Fruit.csv', encoding="latin1")
print(cal)

# Add the labels in pie chart
name = ["Asparagus", "Bell Pepper", "Broccoli", "Carrot" , "Cauliflower", "Celery", "Cucumber", "Green"]

# Plotting pie chart with values
plt.figure()
plt.pie(cal["Calories"], labels=name, autopct='%1.1f%%')
plt.title("Total calories of all fruit and veges ")
plt.show()





"""
  HISTOGRAM PLT
"""


# Read dataset in file in csv format
covid = pd.read_csv('Covid_19_SG.csv')
print(covid)

# Plotting 2 histograms with plots 
plt.figure(figsize=(8,8))
plt.hist(covid["Total Completed Isolation MOH report"], label="Total Completed Isolation MOH report", alpha=0.8, bins=5)
plt.hist(covid["Total Hospital Discharged MOH report"], label="Total Hospital Discharged MOH report", alpha=0.8 ,bins=5)
plt.legend()

# Adding the labels of X and Y 
plt.xlabel("Number of patient")
plt.ylabel("Frequency")
plt.show()








