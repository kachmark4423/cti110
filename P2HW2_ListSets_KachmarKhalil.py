# CTI-110
# P2HW2 - List and Sets
# Khalil Kachmar 
# 08/21/2020
#

'''Create empty list
   Display "Enter ten numbers"
   Display "Enter First Number:"
   Input First Number
   Append list with first number
   Display "Enter Second Number:"
   Input Second Number
   Append list with second number
   .
   .
   .
   Display "Enter Tenth Number:"
   Input Tenth Number
   Append list with tenth Number

   Display "Lowest Number Entered: "
   Display "Highest Number Entered: "
   
   Set sum_list = num1 + num2 + ... + num10
   Display "Sum: sum_list"
   
   set average = sum_list / len(list)
   Display "Average: average"

   Set set_nums = set(list)
   Display set_nums
'''
list_of_nums = []

print("Enter Ten Numbers")

for i in range(1, 11):
	if i == 1:
		num = float(input('\nEnter 1st Number: '))
		list_of_nums.append(num)
	elif i == 2:
		num = float(input('Enter 2nd Number: '))
		list_of_nums.append(num)
	elif i == 3:
		num = float(input('Enter 3rd Number: '))
		list_of_nums.append(num)
	else: 
		num = float(input(f'Enter {i}th Number: '))
		list_of_nums.append(num)


min = min(list_of_nums)
max = max(list_of_nums)

sum_list = 0
for num in list_of_nums:
	sum_list += num

average = sum_list / len(list_of_nums)

print(f'\nLowest Number Entered: {min}')
print(f'Highest Number Entered: {max}')
print(f'The Total of the Numbers Entered: {sum_list}')
print(f'The Average of the Numbers Entered: {average}')

set_nums = set(list_of_nums)
print(f'\nSet Content: {set_nums}')



