known_users = ['Alice', 'Bob', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']

while True:
	print('Hi! My name is Travis')
	name = input('What is your name?:').strip().capitalize()

	if name in known_users:
		print('Hell0{}'.format(Name))
		remove = input('would you like to be removed from the system (y/n)?').strip().lower()

		if remove == 'y':
			known_users.remove(name)
		elif remove == 'n':
			print('No problem.')

	else:
		print("I don't think I have met you yet{}".format(name))
		add_me = input("Would you like to be added (y/n)?").strip().lower()
		if add_me == 'y':
			known_users.append(name)
		elif add_me == 'n':
			print('No worries!')	