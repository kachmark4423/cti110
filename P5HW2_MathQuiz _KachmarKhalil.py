"""
Khalil Kachmar
P5HW2
9-16-2020
Menu driven program that will generate 'random' addition/subtraction problems for user to solve.

Display "Welcom to Math Quiz"
Call menu()
	Display "Main Menu"=
	Display 1)Add Random Numbers
			2)Subtract Random Numbers
			3)Exit
	If 1 Then
		Call add()
			Set num_1 = randomInteger(1, 100)
			Set num_2 = randomInteger(1, 100)
			Display "Num_1 + Num_2"
			Set answer = Num_1 + Num_2
			Display "Enter the sum:"
			Input guess
			Set attempts = 1
			if guess == answer:
				Display "congratulations!!!!"
			else:
				if guess < answer:
					Display "Sorry, guess is too low."	
				if guess > answer:
					Display "Sorry, guess is too high."
				Set correct = False
				while not correct:
					Set attempts = attempts + 1
					Display "Try again:" 
					Input guess
					if guess < answer:
						print("Sorry, guess is too low.")	
					if guess > answer:
						print("Sorry, guess is too high.")
					if guess == answer:
						print("congratulations!!!")
		Display attempts
		Call menu()
	End If

If 2 Then
	Call subtract()
		Set num_1 = randomInteger(1, 100)
		Set num_2 = randomInteger(1, 100)
		Display "Num_1 - Num_2"
		Set answer = Num_1 - Num_2
		Display "Enter the difference:"
		Input guess
		Set attempts = 1
		if guess == answer:
			Display "congratulations!!!!"
		else:
			if guess < answer:
				Display "Sorry, guess is too low."	
			if guess > answer:
				Display "Sorry, guess is too high."
			Set correct = False
			while not correct:
				Set attempts = attempts + 1
				Display "Try again:" 
				Input guess
				if guess < answer:
					print("Sorry, guess is too low.")	
				if guess > answer:
					print("Sorry, guess is too high.")
				if guess == answer:
					print("congratulations!!!")
	Display attempts
	Call menu()
End If

If 3 Then
	Exit
End If
"""

import random
from random import randint
def menu():
	print("\nMain Menu")
	print("----------------")
	print("\n1)Add Random Numbers\n2)Subtract Random Numbers\n3)Exit")

	choice = input("Please choose one of the menu options: ")
	if choice == '1':
		add()
	if choice == '2':
		subtract()
	if choice == '3':
		pass

def add():
	
	num_1 = randint(1, 100)
	num_2 =randint(1, 100)
	print(f'  {num_1}\n+ {num_2}')
	answer = int(num_1) + int(num_2)
	guess = int(input("Enter the sum: "))
	attempts = 1
	
	if guess == answer:
		print("congratulations!!!!")
	else:
		if guess < answer:
			print("Sorry, guess is too low.")	
		if guess > answer:
			print("Sorry, guess is too high.")
		correct = False
		while not correct:
			attempts += 1 
			guess = int(input("\nTry again: "))
			if guess < answer:
				print("Sorry, guess is too low.")	
			if guess > answer:
				print("Sorry, guess is too high.")
			if guess == answer:
				print("congratulations!!!")
				correct = True
	print(f"Attempts: {attempts}")
	menu()

def subtract():
	num_1 = randint(1, 100)
	num_2 = randint(1, 100)
	print(f'  {num_1}\n- {num_2}')
	answer = int(num_1) - int(num_2)
	guess = int(input("Enter the difference: "))
	attempts = 1

	if guess == answer:
		print("congratulations!!!!")
	else:
		if guess < answer:
			print("Sorry, guess is too low.")	
		if guess > answer:
			print("Sorry, guess is too high.")
		correct = False
		while not correct:
			attempts += 1
			guess = int(input("\nTry again: "))
			if guess < answer:
				print("Sorry, guess is too low.")	
			if guess > answer:
				print("Sorry, guess is too high.")
			if guess == answer:
				print("congratulations!!!")
				correct = True
	print(f"Attempts: {attempts}")
	menu()

def main():
	print("Welcome to Math Quiz")
	menu()
	

if __name__ == '__main__':
	main()