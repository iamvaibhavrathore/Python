# Find, index, isalpha, isdigit, isalnum

v="Vaibhav Rathore"
d="12344"
print(v.find('a',2)) # Find 'a' start with 2

print(v.index('R',4))

print(v.isalpha()) #it read space too so that is gives flase
print(d.isdigit()) # all are digit
d="Vaibhav2002"
print(d.isalnum()) #combination of char and digit but not applicable for special element 
