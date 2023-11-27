from itertools import product
a='A B C D E F'
num=3
mylist=[x for x in a if x!=' ']
for roll in product(mylist, repeat=3):
    print(''.join(str(el) for el in roll))
