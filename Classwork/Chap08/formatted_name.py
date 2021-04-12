def get_store_name(first, third, second=''):
	if second:
		full_store = f"{first} {second} {third}"
	else:
		full_store = f"{first} {third}"

	return full_store.title()

store = get_store_name('Mr', 'price')
print(store)
store = get_store_name('Pick', 'pay', 'n')
print(store)