name = "John"
age = str(30)
city = "Birmingham"
ageint = 27

print(name + " is " + age + " years old and is from " + city)

print (name + " is " + str(ageint) + " years old") #using the cast inline here does not change the type, unlike using it when setting the variable.

print (type(age))

age = 12 # This will change the type to an int.

print (type(age))

print (type(ageint))