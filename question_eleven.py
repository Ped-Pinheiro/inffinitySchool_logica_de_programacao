# Make a code to get two integer numbers and one real number. Calculate e show:

# a. The product of double of first with half of second.
# b. The sum of triple of first with the third.
# c. The third with **3

number_one = int(input('Digit a integer number: '))
number_two = int(input('Digit a second integer number: '))
number_three = float(input('Digit a real number: '))

letter_a = (number_one * 2)/(number_two/2)
letter_b = number_one * 3 + number_three
letter_c = number_three**3


print(f'The product of double of first with half of second is: {letter_a}')
print(f'The sum of triple of first with the third is: {letter_b}')
print(f'The third with **3 is: {letter_c}')