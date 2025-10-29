s={1,2,3,4} #It's unordered, unique and unindexed
print(type(s))
s.add(5)
print(s)
s.add(3) #duplicates not allowed
print(s)
s.remove(2)
print(s)
#s.remove(10) #throws error if element not found
s.discard(10) #does not throw error if element not found
print(s)
print(len(s))
x=s.pop() #removes and returns an arbitrary element
print(x)
print(s)
s.clear()
print(s)

b={4,5,6,7}
s={1,2,3,4}
print(s.union(b))
print(s.intersection(b))
print(s.difference(b))
print(s.symmetric_difference(b))
print(s.issubset(b))
print(s.issuperset(b))

c=set([1,2,2,3,4,4,5,5,5])
print(c)