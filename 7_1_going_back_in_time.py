inheritance = float(input())
year = int(input())
yearly_expenditure = 0
total_expenditure = 0
age_counter = 17
for number in range(1800, year + 1):
    age_counter += 1
    if number % 2 == 0:
        yearly_expenditure += 12000
    else:
        yearly_expenditure += 12000 + 50 * age_counter
total_expenditure += yearly_expenditure
difference = inheritance - total_expenditure
if difference >= 0:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {abs(difference):.2f} dollars to survive")