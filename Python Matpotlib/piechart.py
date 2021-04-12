import matplotlib.pyplot as plt

values= [1,2,3,4,5]

labels = ['Python', 'ruby', 'Java', 'React', 'JS']
colors = ['green', 'red', 'purple', 'orange', 'yellow']
pieexlode = [0.3,0,0,0,0]

plt.pie(values,labels=labels,startangle = 90,shadow = True,colors = colors,explode = pieexlode)
plt.title('Pie Chart')
plt.xlabel('Horizontal Title')
plt.ylabel('Vertical Title')
plt.legend(loc= 'best')
plt.show()