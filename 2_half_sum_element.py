from sys import maxsize

n = int(input())
sum_value = 0
value = 0
max_value = -maxsize

for number in range(1, n + 1):
    value = int(input())
    sum_value += value
    if value > max_value:
        max_value = value

difference = abs(max_value - (sum_value - max_value))
if difference == 0:
    print("Yes")
    print(f"Sum = {max_value}")
else:
    print("No")
    print(f"Diff = {difference}")


