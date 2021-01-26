#for eveNum in even_numbers:
		#print(f"\n\t{eveNum}")

squares =[]
for value in range(1,11):
	square = value **4
	squares.append(square)
print(squares)  

print(max(squares))




digits = [1, 2, 3, 4, 5, 6, 7]
print(min(digits))
print(max(digits))
print(sum(digits))

players = ['Charles', 'kingston', 'James', 'Steve', 'Jack', 'Riley', 'Ian', 'Phil']
print(players[0:3])
print(players[-3])

print("Here are the first three players on my team:")
for player in players[:3]:
	print(f"\t{player.title()}")