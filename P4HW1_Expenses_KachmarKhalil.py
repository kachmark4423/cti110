# Program will prompt for initial account amount and expenses and will calculate and ouput amount after expenses. 
# 08/22/2020
# CTI-110 P4HW1 - Expenses
# Khalil Kachmar
#

'''
Display "Enter starting amount in account $"
Input starting_amount
Display "Enter expense 1: "
Input expense
Display Do you want to enter another expense?(y/n)
Input more
Continue to prompt unil more = 'n'
Set withdrawls = expense 1 + ... + expense n
Set new_total equal to starting_amount - withdrawls
Display "The amount in account before expenses subtracted $"starting_amount
Display "Number of expenses entered:" num_expenses
Display "Amount in account after expenses is $"new_total
'''

def expenses():
	expense_list = []
	i = 1
	expense = float(input(f'\nEnter expense {i}: '))
	expense_list.append(expense)
	i += 1
	more = input('Do you want to enter another expense?(y/n) ')
	if more != 'y'and more != 'n':
	 	more = input('Do you want to enter another expense?(y/n) ')
	while more == 'y':
		expense = float(input(f'\nEnter expense {i}: '))
		expense_list.append(expense)
		i += 1
		more = input('Do you want to enter another expense?(y/n) ')
	
	return (expense_list, i)

def get_new_total(starting_amount, expenses):
	
	withdrawls = 0
	for amount in expenses[0]:
		withdrawls += amount

	new_total = starting_amount - withdrawls
	return (new_total, expenses[1])
	

def main():
	starting_amount = float(input('Enter starting amount in account $'))
	money_out = expenses()
	new_total = get_new_total(starting_amount, money_out)[0]
	num_expenses = get_new_total(starting_amount, money_out)[1] - 1

	print(f"\nThe amount in account before expenses subtracted ${starting_amount}")
	print(f"Number of expenses entered: {num_expenses}")
	print(f"Amount in account after expenses is ${new_total}")


if __name__ == "__main__":
	main()