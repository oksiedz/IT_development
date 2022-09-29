from game_data import data
from random import choice

print(data)

new1 = choice(data)
data.remove(new1)
new2=new1['name']
print(data)
print(new1)
print(new2)