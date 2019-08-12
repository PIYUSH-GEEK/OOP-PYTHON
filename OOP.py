class Students:
	def __init__(self, name, age):
		
	        #init is used to initialize the function
		#Make sure the first parameter will always be 'self'
		
		self.name = name
		self.age = age
s1 = Students('John', 23)
s2 = Students('Kevin', 21)

#This will print the name and the age of first student (s1)
print (s1.name, s1.age)

#This will print the name and the age of second student (s2)
print(s2.name, s2.age)

#s1.name and s1.age is referring to self.name and self.age
