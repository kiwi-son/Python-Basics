def add(a,b, plus=0): #plus is a default argument if we don't pass any value it will take 0 as default
    return a + b + plus
print(add(2,3))
print(add(2,3,4))

c=add(b=5, a=10) #keyword arguments
print(c)