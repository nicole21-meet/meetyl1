class Person:
	def __init__(self,name,age,city,gender):
		self.age=age
		self.name=name
		self.city=city
		self.gender=gender
	def eat(self,food):
		print(self.name+ ' is eating '+ food)
	def gender(self):
		
natalie=Person('natalie',16,'beit shemesh','female')
natalie.eat('pizza')

