known_users = ['Alice','Bob','Claire','Dan','Emma','Fred','Georgie','Harry']

print(len(known_users))

while True:
	print('Hi my name is Travis')
	name = input('What is your name?: ').strip().capitalize()

	if name in known_users:
		print('Hello {}!'.format(name))
		# print('name recognised')
		remove = input('would you like to be removed from the system (y/n)?: ').lower()

		if remove == 'y' :
			print(known_users)
			known_users.remove(name)
			print(known_users)

		elif remove == 'n':
			print("No problem, i don't want you to leave anyway!")

	else:
		print("Hmm i don't think i have met you yet {}".format(name))
		add_me = input("would you like to be added to the system (y/n)?").strip().lower()
		if add_me == "y":
			print(known_users)
			known_users.append(name)
			print(known_users)
		elif add_me == "n":
			print('No worries, see you around!')