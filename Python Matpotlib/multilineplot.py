import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
x2 = [1,2,3,4,5]
x3 = [1,2,3,4,5]
y1 = [1,2,4,8,16]
y2 = [1,3,9,13,16]
y3 = [2,4,6,8,10]

plt.plot(x1, y1, 'ro--',label = 'Line 1' )
plt.plot(x2,y2, 'g^-',label = 'Line 2')
plt.plot(x3,y3, 'b-',label = 'Line 3')
plt.legend(loc = 'best')
plt.title('Your title')
plt.xlabel('Horisontal title')
plt.ylabel('Vertical Title')
plt.show()