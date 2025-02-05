import json
import matplotlib.pyplot as plt

with open('data.json', 'r') as file:
    data = json.load(file)

title = data['descriptor']['title']
x_label = data['descriptor']['x-axis label']
y_label = data['descriptor']['y-axis label']

# Extract data for plotting
x_values = data['data']['x']
y_values = data['data']['y']


plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, '-')

plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.grid(True)
plt.show()