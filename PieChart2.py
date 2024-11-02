import matplotlib.pyplot as plt

flavors = ('Vanilla','Chocolate','Strawberry','Blueberry','Apple')
votes = (23,20,15,12,18)

plt.pie(votes, labels=flavors, autopct = '%1.1f%%', )
plt.show()