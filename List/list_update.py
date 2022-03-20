print("******* Replace ********")
l=[20,30,40,50,60,70,80]
l[2]=99
print(l)

print("******** insert ********")
l.insert(0,10) #value unser kr dega given index ke phle
print(l)

print("******* append ********")
l.append(70) # append humesa last me add hoga
print(l)

n=[23,34,45] # measted list
l.append(n)
print(l)

print("********* Extend *********")
l.extend(n) # pure data type ko utha k pass kr deta h
print(l)
