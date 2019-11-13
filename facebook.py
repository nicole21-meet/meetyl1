class User:
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friend_list = []
		self.posts = []
	def add_friend(self,email):
		self.friend_list.append(email)
		print(self.name+' has added '+ email+'as a friend')
	def remov(self,email):
		friend_list.remove(email)
		print(self.name+' has removed '+ email+'from his friend list')
	def new_post(self,text):
		self.posts.append(text)
		print(self.name+'has posted:'+text)
	def get_userInfo (self):
		print('Name:'+self.name)
		print('email:'+self.email)
		print('password:'+self.password)
		print("friend:"+str(self.friend_list))
		print("posts:"+str(self.posts))

user1=User('nicole','nicolekit@gmail.com','12345')
user1.add_friend('natalie')
user1.new_post('heyyy how are yall')
user1.get_userInfo()










