users=[]
posts=[]
class User(object):
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friend_list = []
		users.append(self)
	def add_friend(self,email):
		self.friend_list.append(email)
		print(self.name+' has added '+ email+'as a friend')
	def remov(self,email):
		friend_list.remove(email)
		print(self.name+' has removed '+ email+'from his friend list')
	def add_post(self,):
		post1=Post(text,self.email)
		posts.append(post1)
		print(self.name+'has posted:'+text)
	def get_userInfo (self):
		print('Name:'+self.name)
		print('email:'+self.email)
		print('password:'+self.password)
		print("friend:"+str(self.friend_list))



class Post(object):
	def __init__(self,text,autor):
		self.text=text
		self.autor=author
user1=User('nicole','nicolekit@gmail.com','12345')
user1.add_friend('natalie')

user1.get_userInfo()
		
	 
	
		






















