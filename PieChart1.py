import matplotlib.pyplot as plt

flavors = ('Vanilla','Chocolate','Strawberry','Blueberry','Apple')
votes = (23,20,15,12,18)

plt.pie(votes, labels=flavors)
plt.show()