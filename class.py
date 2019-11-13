class Parrot:
	def __init__(self,name,age,color):
		self.name=name
		self.age=age
		self.color=color

	def fly(self):
		print(self.name+ " " + "is flying")

parrot1 = Parrot("mike",7, 'green')
parrot2 = Parrot("charlie",5, 'red')
print(parrot1.name , parrot1.age)
print(parrot2.name,parrot2.age)
parrot1.fly()
parrot2.fly()

