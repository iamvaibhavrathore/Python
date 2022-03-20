# koi bhi value string ke bich me add kr skte h
txt1= "Empire of {name1} {name2}".format(name1="Vaibhav",name2="Rathore")
print(txt1)

txt2="Empire of {} {}".format("Vaibha","Rathore")
print(txt2)

txt3="Empire of {a:^10} {b}".format(a="Vaibhav",b="Rathore") # b ko size de skte h:10>> 10 total no of space le rho h
# (a:^10) >> char bich me ayega
# (a:<10) >> char left me ayega
# (a:>10) >> char right me ayega
print(txt3)


