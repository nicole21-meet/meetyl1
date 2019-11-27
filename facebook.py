users=[]
posts=[]
loggedin=[]
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
	def get_userInfo (self):
		print('Name:'+self.name)
		print('email:'+self.email)
		print('password:'+self.password)
		print("friend:"+str(self.friend_list))



class Post(object):
	def __init__(self,text,autor):
		self.text=text
		self.autor=author
		print()
		posts.append(self)

		comments=[]
		

class comment(Post):
	def comment(self,text):
		print(text.self)
		append.comments()

def login():
 	print('log in')	
 	email=input('your email')
 	password=input('your pasword')
 	for user in users:
 		if email==User.email:
	 		if password==User.password:
	 			logdin=user


while 0==0:
	option=input('what do you wanna do')
	if option=='login':
		login()
		
	elif option=='sign up':































