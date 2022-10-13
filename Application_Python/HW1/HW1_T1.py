import matplotlib.pyplot as plt
import numpy as np

arrayX = np.random.randint(0, 100, 100)
arrayY = np.random.randint(0, 100, 100)

# Line
plt.plot(arrayY, linestyle='dotted')
plt.xlabel("Distribution")
plt.ylabel("Y-axis")
plt.show()
# Scatter
plt.scatter(arrayX, arrayY, color="blue")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#Bar - Stacked
array100 = range(1, 101, 1)
array201 = range(1, 201, 2)
array202 = range(2, 202, 2)
plt.bar(array100, arrayX, color='r')
plt.bar(array100, arrayY, bottom=arrayX, color='b')
plt.show()
# Bar - unstacked ??
plt.bar(array201, arrayX, color='b')
plt.bar(array202, arrayY, color='r')
plt.show()
# Histogram
fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)
axs.hist(arrayX, bins=20)
plt.show()
# Area
plt.stackplot(array100, arrayX, arrayY, labels=['X', 'Y'])
plt.show()
# Pie
plt.pie(arrayX)
plt.show()
# Violin
plt.violinplot(arrayX)
plt.show()
