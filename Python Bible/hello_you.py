# Ask user for name
name = input("What is your name?: ")

# Ask user for age
age = input('WHat is your age?: ')

# Ask user for city
city = input('What city do you live in ?: ')

# Ask user what they enjoy
love = input('what do you love?: ')

# Create output text
string = 'Your name is {} and you are {} years old. You live in {} aand you love {}'
output = string.format(name,age,city,love)

# Print Output to screen
print(output)