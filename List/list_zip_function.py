l=[1,2,3,4]
k=[5,6,7,8,9]

t=len(l)

for a,b in zip(l,k):   # 2 list ek sath pass kr skta h
    print(a,b)

# By logic 

for h in range(t):
    print(l[h], k[h])