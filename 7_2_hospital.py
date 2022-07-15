number_of_days = int(input())
counter_days = 0
treated_patients_last_three_days = 0
untreated_patients_last_three_days = 0
total_treated_patients = 0
total_untreated_patients = 0
number_doctors = 7
for number in range(1, number_of_days + 1):
    sick_patients = int(input())
    counter_days += 1
    if counter_days == 3:
        if treated_patients_last_three_days < untreated_patients_last_three_days:
            number_doctors += 1
            treated_patients_last_three_days = 0
            untreated_patients_last_three_days = 0
    if sick_patients <= number_doctors:
        treated_patients_last_three_days += sick_patients
        total_treated_patients += sick_patients
    else:
        treated_patients_last_three_days += number_doctors
        total_treated_patients += number_doctors
        untreated_patients_last_three_days += sick_patients - number_doctors
        total_untreated_patients += sick_patients - number_doctors
print(f"Treated patients: {total_treated_patients}.")
print(f"Untreated patients: {total_untreated_patients}.")



