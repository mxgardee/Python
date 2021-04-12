import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

colors = ['green', 'red', 'pink', 'orange', 'yellow']

plt.bar(x1,y1, edgecolor = 'black',color = colors,linewidth = 2) # vertical
# plt.barh(x1,y1) Horisontal
plt.title('Chart Title')
plt.xlabel('Horizontal Title')
plt.ylabel('Vertical Title')
plt.show()