import matplotlib.pyplot as plt

# bar
x1 = [1,2,3,4,5,6]
y1 = [4,5,3,2,1,3]

# line
x2 = [1,2,3,4,5,6]
y2 = [5,3,3,2,1,3]

# bars with colors
plt.bar(x1, y1, label="Bars", color="orange")
plt.plot(x2, y2, label="Lines", color="red")

# legends with location
plt.legend(loc="upper left")

plt.show()