import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

colors = ['green', 'red', 'pink', 'orange', 'yellow']

plt.plot(x1,y1,'ro--',label= 'Students')
plt.title('Chart Title')
plt.xlabel('Horizontal Title')
plt.ylabel('Vertical Title')
plt.legend(loc='best')
plt.grid(which= 'major',linestyle = '-',color= 'black')
plt.minorticks_on()
plt.grid(axis = 'x' ,which= 'minor',linestyle= '--',color= 'grey',alpha = 0.2)
plt.show()