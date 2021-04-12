# Functions:

def add(x,y):
	return x + y

add(5,10)

awnser = add(7,7)
print(awnser)

# word = 'pen'
# word[::-1]

def rev(text):
	return text[::-1]


rev('pen')
print(rev([1,2,3,4]))

# Variable scopes:

a = 100 #Global scope!

def f1():
	a = 200 #local variable overiades the global ,only in function
	print(a) 

def f2():
	# change the global 
	global a
	a = 250
	print(a)

f1()
f2()
print(a)

# def about(name,age,likes):
# 	sentence = 'Meet {}!they are {} years old and they like {}'.format(name,age,likes)
# 	# return sentence
# 	print(sentence)

# about('Jack',23,'Python')
# random order
# about(age = 23, name = "Jack",likes = 'Python')

def about(name,age,likes = 'Python'):
	sentence = 'Meet {}!they are {} years old and they like {}'.format(name,age,likes)
	# return sentence
	print(sentence)

# over writes the Python from likes.
about('Jack',23,'Football')