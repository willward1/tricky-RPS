import random
import sys

print("Welcome to Tricky Rock Paper Scissors. A couple of questions before we begin:")

while True:
	print("Are you male or female? Enter \"m\" for male and \"f\" for female")
	gen = input()
	if gen == "m" or gen == "f":
		break
	else:
		print('Invalid input. Enter "m" or "f"')

while True:
	print('How experienced are you at this game? Enter "1" for inexperienced, or "2" if you\'re a pro')
	exp = input()
	if exp == "1" or exp == "2":
		break
	else:
		print('Invalid input. Enter "1" or "2"')

choices = ('R', 'P', 'S')  

while True:
	print('Enter R for rock, P for paper or S for scissors')
	throw = str(input())
	throw = throw.upper()
	if throw in choices:
		print("Ok, let's do this...")
		break
	else:
		print("Invalid selection, try again.")


# RANDOM GAME (1 = rock, 2 = scissors, 3 = paper)

comp = random.randint(1,3)
if comp == 1:
	cplay = 'CR'
elif comp == 2: 
	cplay = 'CS'
else:
	cplay = 'CP'	

# WEIGHTED GAME, assumes males will throw rock 

x = random.randint(1, 100)

if x <= 75:
    cplay = 'CP'
elif x > 76 and x <= 87:
    cplay = 'CS' 
else:
    cplay = 'CR'

def rps(throw, cplay):
	if throw == 'R' and cplay == 'CR':
		print('You both threw rock, it was a tie!')
	if throw == 'R' and cplay == 'CS':
		print("Your rock crushes the computer's scissors. You win!")
	if throw == 'R' and cplay == 'CP':
		print("Oh no! Your rock has been covered by the computer's paper. You lose!")
	if throw == 'P' and cplay == 'CR':
		print("Your paper covers the computer's rock. You win!")
	if throw == 'P' and cplay == 'CS':
		print("Oh no! Your paper is sliced by the computer's scissors. You lose!")
	if throw == 'P' and cplay == 'CP':
		print("You both threw paper. It was a tie!")
	if throw == 'S' and cplay == 'CR':
		print("On no! Your scissors have been crushed by the computer's rock. You lose!")
	if throw == 'S' and cplay == 'CS':
		print("You both threw scissors. It was a tie!")
	if throw == 'S' and cplay == 'CP':
		print("Your scissors slice through the computer's paper. You win!")

if gen == 'f':
	rps(throw, cplay)
elif gen == 'm':
	rps(throw, cplay)
	