schools = {
	'Ligbron': {
	'Name' : 'Ligbron Academy',
	'Type' : 'Secondary school',
	'Location' : 'Ermelo',
	'Class' : 'Model C'","
	},
	'CodeCollege': {
	'Name' : 'Code College',
	'Type' : 'Tertiary',
	'Location' : 'Woodmead',
	'Class' : 'Private',
	},
}

for username, school_info in schools.items():
	print(f'\nUsername: {username}')
	school_ID = f"{school_info['Name']} {school_info['Location']}"
	Type = school_info['Type']
	print(f'\tschool_ID: {school_ID.title()}')
	
	print(f'\tType: {Type.title()}')