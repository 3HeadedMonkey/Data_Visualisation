import matplotlib.pyplot as plt

# Set tables
x_values = list(range(1,5001))
y_values = [x*x*x for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=20)

# Set chart
plt.title("3rd Power", fontsize=25)
plt.xlabel("x values", fontsize=10)
plt.ylabel("y values", fontsize=10)

# Tick labels
plt.tick_params(axis='both',which='minor',labelsize=10)

plt.show()
