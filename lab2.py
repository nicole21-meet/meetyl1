
def commonlist(list1,list2):
	common_num=[]
	for number in list1:
		if number in list2:
			common_num.append(number)
	return common_num
b=input('numbers')
c=input('numbers')
a=commonlist(b,c)
print(a)