#mile_age = cars_1.get('mileage', 'Not Applicsble')
#print(mile_age)
#engine_type = cars_1.get('engine', 'Not Applicable')
#
cars_list = {'BMW': 'Black',
			'Mercedes': 'Red',
			'Audi': 'Blue',
			'Lambo': 'Red',}
for car, lists in cars_list.items():
	print(f'{car.title()} is {lists.title()}')

for car in cars_list.keys():
	print(car.title())	

for car in cars_list.values():
	print(car.title())

for car in sorted(cars_list.keys()):
	print(f'{car.title()}, is manufactured by Germans.')

print('set values:')
for car in set(cars_list.values()):
	print(car.title())