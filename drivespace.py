import requests
import matplotlib.pyplot as plt
from datetime import datetime

drive = 'C:'
response = requests.get(f'http://localhost:3000/getdrivespace?drive={drive}')
data = response.json()

total_gb = data['total'] / (1024 ** 3)  # 1 GB = 1024^3 bytes
available_gb = data['available'] / (1024 ** 3)
used_gb = total_gb - available_gb

plt.figure()
plt.bar([drive], [used_gb], label='Used', color='r')
plt.bar([drive], [available_gb], bottom=[used_gb], label='Available', color='g')

plt.ylabel('Space (GB)')
plt.title(f'Drive {drive} Space Usage')
plt.legend()

plt.text(0, used_gb / 2, f'{used_gb:.2f} GB', ha='center', va='center', color='white')
plt.text(0, used_gb + (available_gb / 2), f'{available_gb:.2f} GB', ha='center', va='center', color='black')

current_datetime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

plt.savefig(f'Cdrive_space_{current_datetime}.png', dpi=300, bbox_inches='tight')
plt.close()