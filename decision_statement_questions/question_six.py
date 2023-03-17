# Make a code to compare three numbers and shows the grater number

number_one = int(input('Digit the first number: '))
number_two = int(input('Digit the second number: '))
number_three = int(input('Digit the third number: '))

if number_one > number_two and number_one > number_three:
    print(f'The number {number_one} is grater than {number_two} and {number_three}')

elif number_two > number_one and number_two > number_three:
    print(f'The number {number_two} is grater than {number_one} and {number_three}')

else:
    print(f'The number {number_three} is grater than {number_one} and {number_two}')