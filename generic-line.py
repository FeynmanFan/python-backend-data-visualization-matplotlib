import json
import matplotlib.pyplot as plt

with open('data.json', 'r') as file:
    data = json.load(file)

# get descriptor
title = data['descriptor']['title']
x_label = data['descriptor']['x-axis label']
y_label = data['descriptor']['y-axis label']

# get the actual data
x_values = data['data']['x']
y_values = data['data']['y']

# plot it
plt.figure()
plt.plot(x_values, y_values, '-')

plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.show()