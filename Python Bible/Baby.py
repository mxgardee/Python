from random import choice

questions = ['why is the sky blue?: ','how do cars drive?: ','may I come with?: ','when are they comming?: ']

question = choice(questions)
awnser = input("Hello I am baby! Whats your name?: ").lower()

while awnser != 'just because':
	awnser = input('why?: ').strip().lower()

print('Oh...Ok')