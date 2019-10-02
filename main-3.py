import matplotlib.pyplot as plt

# random values
stock_price = [5,22,33,21,24,22,45,43,54,21,22,33,44,55,66,43,21,44,54]

# bins are used for sorting values into what they represent
bins = [0,10,20,30,40,50,60,70,80]

plt.hist(stock_price, bins, histtype='bar', rwidth=0.8)

plt.show()