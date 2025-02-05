import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('data.xlsx', sheet_name='Data')

days = data['Days'].tolist()
cars = data['Cars on Street'].tolist()

plt.figure()
plt.plot(days, cars)
plt.title("My Plot")
plt.show()