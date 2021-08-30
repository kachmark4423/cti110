# Program will prompt for cost of meal and tip percentage and dispaly meal cost, tax amount, tip amount, and total.
# 08/22/2020
# CTI-110 P3HW2 - MealTipTax
# Khalil Kachmar
#

#Dispaly "Enter food cost:"
#Input cost

#Display "Enter tip percentage:"
#Input tip percentage

#Set tip_amount = tip_percentage * 0.01 * food_cost
#Set tax_amount = 0.06 * food_cost
#Set total_cost = food_cost + tip_amount + tax_amount

#Display "Meal price: cost"
#Display "Tax: tax_amount"
#Display "Tip: tip_amount"
#Display "Total: total"




def tip(cost, percentage):
	tip_options = (15, 18, 20)
	if percentage not in tip_options:
		while percentage not in tip_options:
			percentage = int(input('Please enter tip amount of 15, 18 or 20 only: '))
	 	
	tip_amount = cost * percentage * .01
	return tip_amount

def tax(cost):
	tax_amount = cost * .06
	return tax_amount
	

def main():
	meal_cost = float(input('Please enter cost of meal: '))
	tip_percentage = int(input('Enter tip amount of 15, 18 or 20: '))
	
	tip_amount = tip(meal_cost, tip_percentage)
	tax_amount = tax(meal_cost)
	total = meal_cost + tax_amount + tip_amount

	print(f'\nMeal price: {meal_cost}')
	print(f'Tax: {tax_amount}')
	print(f'Tip: {tip_amount}')
	print(f'Total: {total}')



if __name__ == "__main__":
	main()