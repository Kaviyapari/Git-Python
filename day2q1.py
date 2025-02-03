l=[1,5,"A",66,1,0]
numbers=[x for x in l if isinstance(x, (int,float))]
numbers.sort()
print("sorted numbers:",numbers)