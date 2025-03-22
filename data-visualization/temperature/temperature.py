import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('temperature.csv')

x = df['time']
y = df['temperature']

plt.figure(figsize=(12,5))

plt.plot(x, y, '-b', label='temperature')

plt.title("24 Hour Temperature")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()