from itertools import permutations
a=7
mylist=[x for x in range(1,a+1)]
result=list(permutations(mylist))

with open('solperm.txt','w') as file:
    file.truncate()
    file.write(f'{len(result)}\n')
    for e  in result:
        f=' '.join([str(el) for el in e])
        file.write(f'{f}\n')
    