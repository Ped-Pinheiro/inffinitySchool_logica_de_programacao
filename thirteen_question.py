# Make a code to calculate the ideal weight for Men and Woman.
# a. For Men
# b. For Woman

print('')
height = float(input('Digit your height: '))

ideal_weight_men = (72.7 * height) - 58
ideal_weight_woman = (62.1 * height) - 44.7

print('')
print(f'The ideal weight for Men is: {round(ideal_weight_men,2)}')
print('')
print(f'The ideal weight for Woman is: {round(ideal_weight_woman,2)}')
print('')