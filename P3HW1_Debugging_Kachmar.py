    # Program will prompt for a score and return a letter grade 
    # 08/22/2020
    # CTI-110 P3HW1 - Debugging
    # Khalil Kachmar
    #

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores
    B_score = 80
    C_score = 70
    
    score = float(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')

    else:
        print('Your grade is: F') # TO DO: finish this

# program test
# for i in range(101):
#     grade = i
#     print(grade)
#     main(grade) #Add in argument to main()





# program start
main()

