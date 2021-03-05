#5_1

avail_cars = ['BMW','Mercedes','Audi','Maserati','lmborghini','Volkswagen','Mclaren','Buggati']
requested_cars = ['BMW','Toyota','Mclaren','Lancia']
for requested_car in requested_cars:
	if requested_car in avail_cars:
		print(f'\n{requested_car} is available.')
	else:
		print(f'\n{requested_car} is unavailable.')

print(f'\n\tThank you for coming by!')

#5_2
car = 'bmw'
car == 'bmw'

#cars = 'Audi'
#cars.lower() = "audi"

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!")

answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

#requested_toppings = ['mushrooms', 'onions', 'pineapple']
# 'mushrooms' in requested_toppings
#True
# 'pepperoni' in requested_toppings
# False

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")
	

