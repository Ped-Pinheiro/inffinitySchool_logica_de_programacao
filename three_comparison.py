# Comparison between three numbers.

number_one = int(input("Digit the first number: "))
number_two = int(input("Digit the second number: "))
number_three = int(input("Digit the third: "))

if number_one >= number_two and number_one >= number_three:
    print(f"{number_one} is greater than {number_two} and {number_three}")

elif number_two >= number_one and number_two >= number_three:
    print(f"{number_two} is greater than {number_one} and {number_three}")

elif number_three >= number_one and number_three >= number_two:
    print(f"{number_three} is greater than {number_one} and {number_two}")

# elif number_one < number_two and number_one < number_three:
#     print(f'{number_one} is less than {number_one} and {number_two}')

# elif number_two < number_one and number_two < number_three:
#     print(f'{number_two} is less than {number_one} and {number_three}')

# elif number_three < number_one and number_three < number_two:
#     print(f'{number_three} is less than {number_one} and {number_two}')
