import matplotlib.pyplot as plt

flavors = ('Vanilla','Chocolate','Strawberry','Blueberry','Apple')
votes = (23,20,15,12,18)

warna =('#E67F0D', '#FFF8DC','#8B4513', '#D53032', '#93C572')
explode =(0.1,0,0,0,0)

plt.title ('Most Favorite Jam Flavors')
plt.pie(votes, labels=flavors, autopct = '%1.1f%%', colors = warna, explode=explode, shadow=True )
plt.show()