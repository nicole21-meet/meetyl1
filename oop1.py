class Animal:
	def __init__(self,sound,name,age,fav_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.fav_color=fav_color
	def eat(self,food):
		print('yummy!!' + self.name+ " " + "is eating " + food)
	def discription(self):
		print(self.name +' is '+ str(self.age) + ' years old and loves the color '+ self.fav_color)
	def make_sound(self, amount):
		print(self.sound*int(amount))
dog=Animal('hav ','max',3 ,"red")
dog.eat('meat')
dog.discription()
dog.make_sound(5)

