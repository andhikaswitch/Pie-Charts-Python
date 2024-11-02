import matplotlib.pyplot as plt

flavors = ('Vanilla','Chocolate','Strawberry','Blueberry','Apple')
votes = (23,20,15,12,18)

warna =('#E67F0D', '#FFF8DC','#8B4513', '#D53032', '#93C572')
plt.pie(votes, labels=flavors, autopct = '%1.1f%%', colors = warna )
plt.show()