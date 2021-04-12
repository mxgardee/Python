import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style('darkgrid')

N = 250
x1 = np.random.rand(N)
y1 = np.random.rand(N)

plt.scatter(x1,y1,s = 30)
plt.show()