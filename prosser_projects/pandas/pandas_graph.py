import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "data/ramen-ratings.csv"

name = 'Style'
value = 'Stars'

data = pd.read_csv(file)
name_data = data[name].tolist()
value_data = data[value].tolist()
dictionary: dict = {}


for place in name_data:
	try:
		if not place in dictionary:
			dictionary[place] = value_data.pop(0)
		else:
			dictionary[place] = round(dictionary[place] + value_data.pop(0) / 2)
	except ValueError:
		print("Invalid Value")
	except TypeError:
		print("Invalid Type")


x_values: list = []
y_values: list = []

for item in dictionary:
	x_values.append(item)
	y_values.append(dictionary[item])

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

y_pos = np.arange(len(x_values))

print(x_values)
ax.bar(y_pos, y_values)
plt.xticks(y_pos, x_values)
plt.show()
