import matplotlib.pyplot as plt
x=[10,20,30,50]
y=["c","c++","java","python"]
ex = [0,0.3,0,0]
plt.pie(x,labels=y,explode=ex) #explode is used to highlight a particular part of the pie chart
plt.show()
