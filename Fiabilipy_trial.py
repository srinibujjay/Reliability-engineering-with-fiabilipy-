a=(7,0,0,9,5)
b=(6,7,8,9,10)
def avail1(x):
    for i in a:
     return x[0] or x[i]or x[i+1]

print(avail1(a))