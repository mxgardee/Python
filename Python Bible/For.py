# for number in range(1,11,2):
# 	print(number)

# for letter in 'abcd':
# 	print(letter)



# vowels = 0
# consonants = 0

# for letter in 'Hello':
# 	if letter.lower() in 'aeoiu':
# 		vowels = vowels + 1
# 	elif letter ==" ":
# 		pass
# 	else:
# 		consonants = consonants + 1

# print('There are {} vowels'.format(vowels))
# print('There are {} consonants'.format(consonants))



students = {
	'males':['Tom','Charlie','Harry'],
	'females':['Sarah','Huda','Samantha']
	}

for key in students.keys():
	for name in students[key]:
		if 'a' in name:
			print(name)