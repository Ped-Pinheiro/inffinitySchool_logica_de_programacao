number_one = float(input(f"Digit your first school grade: "))

number_two = float(input(f"Digit your second school grade: "))

total = (number_one + number_two) / 2

if total >= 7:
    print(f"Congratulations, you are approved.")

elif total == 10:
    print(f"Congratulations, you are approved with distinction.")

else:
    print(f"Unfortunately, you are flunked.")
