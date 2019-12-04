users=[]
posts=[]
#DEF THE CLASS
class User(object):
    def __init__(self,name,email,password):
            self.name=name
            self.email=email
            self.password=password
            self.friend_list = []
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
def pr():
    print('menu-')
    print('add friend')


# A MENEO TO GET THE LOG IN SYSTEM AND THE CODE RUNING

while 0==0:
    option=input('what do you wanna do')
    if option=='login':
        print('log in')	
        email5=input('your email')
        for user in users:
            if email5==new_user.email:
                password5=input('your pasword')
                print('yess')
                if password5==new_user.password :
                    print('you logged in succsesfully')
                    

                else:
                    print('wrong username')
            else:
                print('wrong email')
		
    elif option=='sign up':
        name1=input('your name-')
        email1=input('your email-')
        password1=input('your password-')
        new_user = User(name1,email1,password1)
        print(new_user.email)
        users.append(new_user)
        


