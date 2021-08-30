# Program will pick a random number and ask user to try and guess it. 
# 9-11-2020
# CTI-110 P5HW1 - Random Number
# Khalil Kachmar
#
"""
Call menu()
Display "Main Menu
		---------------
		1)Play Game
		2)Exit"
Display "Enter Selection"
Input selection
If selection == 1 Then
	Call game()
End If
Set rand_int = random(1, 100)
Set attempts = 0
Set won = False

While not won
	Display "Enter an integer between 1 and 100:"
	Input guess
	if guess < rand_int Then
			Set attempts = attempts + 1
			Display "Too low, try again."
		Else If guess > rand_int Then
			attempts = attempts + 1
			Display "Too high, try again."
		Else:
			attempts = attempts + 1
			Set won = True
			Display "Congratulations!!!"
			Display "Attempts: attempts"
			Display 'Would you like to play again?(1-yes, 2-no)'
			Input play_again
			If play_again == '1' Then
				Call game()
			End If
			If play_again == '2' Then
				Exit
			End If
	End If
"""
import random 
from random import randrange
def menu():
	print("Main Menu")
	print("------------")
	print('\n1) Play Game\n2) Exit')
	selection = input('\nEnter Selection: ')

	if selection == '1':
		game()
	
def game():
	rand_int = randrange(1, 101)
	attempts = 0
	won = False
	while not won:
		guess = int(input('\nEnter an integer betwen 1 and 100: '))

		if guess < rand_int:
			attempts += 1
			print("Too low, try again.")
		elif guess > rand_int:
			attempts += 1
			print("Too high, try again.")
		else:
			attempts += 1
			won = True
			print("Congratulations!!!")
			print(f"Attempts: {attempts}")
			play_again = input('Would you like to play again?(1-yes, 2-no)')
			if play_again == '1':
				game()
			if play_again == '2':
				break


def main():
	menu()

if __name__ == '__main__':
	main()