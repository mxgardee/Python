def build_person(first_name, last_name, age=None):

	person = {'first': first_name.title(), 'last': last_name.title()}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', 80)
firstName = musician['first']
lastName = musician['last']
myAge = musician['age']
print(f'{firstName} {lastName} {myAge}')