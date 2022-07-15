n = int(input())
salary = int(input())
salary_lost = False
for number in range(1, n +1):
    site_name = input()
    if site_name == "Facebook":
        fine = 150
        salary -= fine
    elif site_name == "Instagram":
        fine = 100
        salary -= fine
    elif site_name == "Reddit":
        fine = 50
        salary -= fine
    if salary <= 0:
        salary_lost = True
        break
if salary_lost:
    print("You have lost your salary.")
else:
    print(salary)

