# Make a program that asks for the temperature in degrees Celsius, transforms it and shows it in degrees Fahrenheit.

celsius = float(input("Digit a number celsius temperature: "))

fahrenheit = celsius * 1.8 + 32

print(f"The temperature in Fahrenheit is: {round(fahrenheit,2)}")
