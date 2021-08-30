  # Program will request user to input two integers and return their sum and product.
    # 08/21/2020
    # CTI-110 P1HW2 - Basic Math
    # Khalil Kachmar
    
    #Display 'Enter first number:'
    #Input first_number
    #Display 'Enter second number:'
    #Input second number
    #Display 'First number entered: first_number'
    #Display 'Second number entered: second_number'
    #Set sum = first_number + second_number
    #set product = first_number * second_number
    #Display 'Sum of both numbers: sum'
    #Display 'Result of multiplying the two numbers: product'

first_number = int(input('Please Enter first number: '))
second_number = int(input('Please Enter second number: '))
print(f'First number entered: {first_number}')
print(f'Second number entered: {second_number}')

sum = first_number + second_number
product = first_number * second_number

print(f'\nSum of both numbers: {sum}')
print(f'Result of multiplying the two numbers: {product}')
