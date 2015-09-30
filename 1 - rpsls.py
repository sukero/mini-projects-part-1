import random

player_choice = input("> ")

# converts the name to number
def name_to_number(name):
	if name == 'rock':
		return 0
	elif name == 'Spock':
		return 1
	elif name == 'paper':
		return 2
	elif name == 'lizard':
		return 3
	elif name == 'scissors':
		return 4
	else:
		print ("plz choose a right one")

#converts the number to name
def number_to_name(number):
	if number == 0:
		return 'rock'
	elif number == 1:
		return 'Spock'
	elif number == 2:
		return 'paper'
	elif number == 3:
		return 'lizard'
	elif number == 4:
		return 'scissors'
	else:
		print ("plz choose a right one")

# the main func
def rpsls(player_choice):
	player_number = name_to_number(player_choice)
	comp_number = random.randrange(0, 5, 1)
	comp_choice = number_to_name(comp_number)

	print("Player chooses %s" %(player_choice))
	print("Computer chooses %s" %(comp_choice))

	if (player_number - comp_number) == 1 or (player_number - comp_number) == 2:
		print ("Player wins!")
	elif (player_number - comp_number) == 3 or (player_number - comp_number) == 4:
		print ("Computer wins!")
	elif (comp_number - player_number) == 1 or (comp_number - player_number) == 2:
		print ("Computer wins!")
	elif (comp_number - player_number) == 3 or (comp_number - player_number) == 4:
		print ("Player wins!")

rpsls(player_choice)

