print(1,2,3,4,5)

numbers = [1,2,3,4,5]
print(numbers)

# unpakking the list:
print(*numbers)

print('abc')

print(*'abc')

# pakking:
# adding more numbers in function
def add(*numbers):
	total = 0
	for number in numbers:
		total = total + number
		# return(total)
		print(total)

add(1,2,3,4,5,6,7,8,9)

def foo(**kwargs):
	for key,value in kwargs.items():
		print('{}: {}'.format(key.title(),value.capitalize()))

foo(huda ='Female',Ziyad ='Male',henry = 'Male')