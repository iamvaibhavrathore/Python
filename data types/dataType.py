#*********** Mutable Data type**************
# List, dictionary, byte array

#*********** Immutable data Type *********
# Int, Float, Complex, String, tuple, set


#**************** integer *************
a=5
print(a,type(a))
a=5.5
print(a,type(a))
a=2+5j
print(a,type(a))

#************** string ************** 

s='vishu@123'
print(s,type(s))
s='''Hello
  welcome to 
   vishus metaverse'''
print(s)

s='10'
print(s)
print(s,type(s))

#************ List *****************

list=[10, 'VR', 2.2]
print(list,type(list))


#************* Tuple ***************

# Ek se jada value rhni chahiye
t=(2,10,'vaibhav')
print(t,type(t))
t=(10)
print(t,type(t))


#************* Dictionary ***********

d = {
    'name':'Vaibhav',
    'last_name': 'rathore'

}
print(d,type(d))
print(d['name'])

#************** Set ***************

first_set={1,2,3,1}
print(first_set) 
print(first_set,type(first_set))


