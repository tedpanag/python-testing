import sys

# Inputs
number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))


# Choose what to do

def calculate():
    mathematical_operation = input('''
What operation would you like to use? :
+ for addition
- for subtraction
* for multiplication
/ for division
^ for powers
''')

# +
    if mathematical_operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

# -
    elif mathematical_operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)


# *
    elif mathematical_operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)


# /

    elif mathematical_operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

# ^
    elif mathematical_operation == '^':
        print('{} ^ {} = '.format(number_1, number_2))
        print(number_1 ^ number_2)


#Skill issue detected
    else:
        print('You have a skill issue, retry the program with normal numbers and operations.')

    again()


#Redo? 
def again():
    calc_again = input('''
Do you want to calculate again?
Type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print("See ya.")
    else:
        again()

calculate()