print("Pizza!")
prompt = "\nEnter your desired toppings:"

active = True
message = ''
toppings = []

while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		toppings.append(messsage)

print(f'\n These are your toppings: {toppings}')
