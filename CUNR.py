from functools import reduce
n=961

print(reduce(lambda x,y: (x*y)%1000000, (2*x+1 for x in range(n-2))))