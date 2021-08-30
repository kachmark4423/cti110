# Program will prompt user for cost of meal, tax and tip percentages and calculate tax and tip amount and total cost
# 08/21/2020
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Khalil Kachmar
#

#Dispaly "Enter food cost:"
#Input cost

#Display "Enter tip percentage:"
#Input tip percentage
#Display "Enter tax percentage:"
#Input tax percentage

#Set tip_amount = tip_percentage * 0.01 * food_cost
#Set tax_amount = tax_percentage * 0.01 * food_cost

#Display "Calculated Tip: tip_amount"
#Display "Calculated Tax: tax_amount"

#Set total_cost = food_cost + tip_amount + tax_amount
#Display "Total cost including tip and tax: total_cost"

food_cost = float(input('Enter Food Cost: '))

tip_percentage = float(input('\nEnter Tip Percentage: '))
tax_percentage = float(input('Enter Tax Percentage: '))

tip_amount = tip_percentage * 0.01 * food_cost
tax_amount = tax_percentage * 0.01 * food_cost

print(f"\nCalculated Tip: {tip_amount}")
print(f"Calculated Tax: {tax_amount}")

total_cost = food_cost + tip_amount + tax_amount
print(f"\nTotal cost including tip and tax: {total_cost}")
