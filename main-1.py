# pyplot is the main component, that is almost always used
import matplotlib.pyplot as plt

x1 = [1,2,3,4,5,6,7]
y1 = [5,4,5,1,3,1,4]

x2 = [1,2,3,4,5,6,7]
y2 = [1,2,3,4,5,6,7]

# this is lists of x and y coordinates
plt.plot(x1,y1, label="x1 and y1")
plt.plot(x2,y2, label="x2 and y2")

# set labels
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("learning matplotlib")

# create legends which distinguish between the x1 and y1 and x2 and y2
plt.legend()

# show the graph
plt.show()