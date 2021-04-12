number = 1

while number <= 10: 
	if number % 2 == 0:		
		print(number)
	number = number + 1

l = [] # list
while len(l) < 3:
	new_name = input('Please add a new name: ').strip().capitalize()
	l.append(new_name)

print('sorry list is full')
print(l)