import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('data.xlsx', sheet_name='Data')

cars = data['Cars on Street'].tolist()
days = data['Days'].tolist()

plt.figure()
plt.plot(days, cars)
plt.title("My Plot")
plt.show()