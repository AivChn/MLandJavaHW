import math
import pandas as pd
from matplotlib import pyplot

data = pd.read_csv('students.csv')

def get_std(datapoints):
    mean = datapoints.mean()

    variance = 0
    for d in datapoints:
        variance += pow(d - mean, 2)

    variance /= len(datapoints)

    return math.sqrt(variance)


age_info = (data['גיל'].min(), data['גיל'].max(), data['גיל'].mean())
grade_info = (data['ציון'].min(), data['ציון'].max(), data['ציון'].mean())

print(f'Age min, max and mean: {age_info}')
print(f'Grade min, max and mean: {grade_info}')

print(get_std(data['גיל']))
print(get_std(data['ציון']))

X = data['גיל']
y = data['ציון']

p = pyplot.plot(X, y, 'o')

pyplot.show()

