# Make a Program that asks how much you earn per hour and the number of hours worked in the month. Calculate and show the total of your salary for that month.

money_per_hour = float(
    input("Digit the money per hour you make from the work: "))
hours_worked = int(input("Digit how many hours you work of a mouth: "))

total = money_per_hour * hours_worked

print(f"The total of salary you gain on a mouth is: {round(total,2)}")
