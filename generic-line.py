import json
import matplotlib.pyplot as plt
from datetime import datetime

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
plt.plot(x_values, y_values, '-', label='Request latency over time')

plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)

thresholds = [3, 4.5]
threshold_labels = ['discount', 'free']

plt.yticks(thresholds, threshold_labels)

plt.grid(linestyle='--', alpha=.5)
plt.subplots_adjust(bottom=.2) # 20% more at the bottom

plt.legend(bbox_to_anchor=(.5, -.18), loc='upper left', borderaxespad=0.0)

current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

plt.savefig(f'generic-line_{current_datetime}.png', dpi=300, bbox_inches='tight')

plt.close()