# Make a code to compare three numbers and shows the grater and lower number

number_one = int(input('Digit the first number: '))
number_two = int(input('Digit the second number: '))
number_three = int(input('Digit the third number: '))

if number_one > number_two and number_one > number_three:
    print(f'The higher number is {number_one}. The Lower number is {number_three}')

elif number_two > number_one and number_two > number_three:
    print(f'The higher number is {number_two}. The Lower number is {number_three}')

else:
    print(f'The higher number is {number_three}. The Lower number is {number_two}')