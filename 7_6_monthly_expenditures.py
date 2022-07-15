month = int(input())
electricity_bill = 0
for number in range(1, month + 1):
    value = float(input())
    electricity_bill += value
water_bill = 20 * month
internet_bill = 15 * month
others_bill = (electricity_bill + water_bill + internet_bill) * 1.2
average_total_bill = (electricity_bill + water_bill + internet_bill + others_bill) / month
print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {others_bill:.2f} lv")
print(f"Average: {average_total_bill:.2f} lv")