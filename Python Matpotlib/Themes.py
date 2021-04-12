  
import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_style('darkgrid')
plt.style.use('ggplot')
print(plt.style.available)

x1=[1,2,3,4,5]
y1 = [1,2,4,8,16]


plt.bar(x1, y1) 
plt.xlabel('Horisontal title')
plt.ylabel('Vertical title')
plt.title('Themes')
plt.show()