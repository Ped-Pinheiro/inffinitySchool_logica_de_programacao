# Make a Program that asks for the temperature in degrees Fahrenheit, transforms it, and shows the temperature in degrees Celsius.

fahrenheit = float(input("Digit a number in Fahrenheit: "))

celsius = 5 * ((fahrenheit - 32) / 9)

print(f"The temperature in celsius is: {round(celsius,2)}")
