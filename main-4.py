# https://medium.com/@andykashyap/top-5-tricks-to-make-plots-look-better-9f6e687c1e08

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

deaths = [1,2,3,4,5,6,7]
causes = [1,2,3,4,5,3,4]

#plt.style.use("classic")

plt.plot(deaths, causes)
plt.legend('ABCDEF', ncol=2, loc='upper left');
plt.show()