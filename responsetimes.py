import requests
import matplotlib.pyplot as plt
from datetime import datetime

response = requests.get('http://localhost:3000/getresponsetimes')
data = response.json()

durations = [item['duration'] for item in data]

plt.figure()
plt.hist(durations, bins=10, edgecolor='black')
plt.title('Response Times')
plt.xlabel('Duration (seconds)')
plt.ylabel('Frequency')

current_datetime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

plt.savefig(f'response_times_{current_datetime}.png', dpi=300, bbox_inches='tight')
plt.close()