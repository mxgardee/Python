import matplotlib.pyplot as plt


x =[1,2,3,4]
y = [2,4,6,8]

plt.plot(x, y, 'g-s') # after  the g(clour) is the type line
# plt.plot([1,2,3,4],[2,4,6,8], 'g-')
plt.axis([0,5,0,10])
plt.xlabel('Horisontal title')
plt.ylabel('Vertical title')
plt.title('My title')
plt.show()