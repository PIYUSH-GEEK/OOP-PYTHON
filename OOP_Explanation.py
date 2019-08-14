class Students:
#Students is the class here

	def __init__ (self, name, age):
	# __init__ is a method
	#In OOP, function is called method
	
		self.name = name
		self. age = age
		#name and age are attributes. You can create your desired attribut.
		
s1 = Students('John', 23)
#class_name(attribute1, attr2,...)
s2 = Students('Kevin', 30)
#class_name(attr1, attr2,...)

#These two are constructors. s1 and s2 are objects here.
#John is going inside 'self.name'. Similarly all the attributes is going to their defined place.

print(s1.name) #object_name.attribute
print(s2.age) #object_name.attribute
