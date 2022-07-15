n = int(input())
counter_n2 = 0
counter_n3 = 0
counter_n4 = 0
result_2 = 0
result_3 = 0
result_4 = 0
for number in range(1, n + 1):
    value = int(input())
    if value % 2 == 0:
        counter_n2 += 1
        result_2 = counter_n2 / n * 100
    if value % 3 == 0:
        counter_n3 += 1
        result_3 = counter_n3 / n * 100
    if value % 4 == 0:
        counter_n4 += 1
        result_4 = counter_n4 / n * 100
print(f"{result_2:.2f}%")
print(f"{result_3:.2f}%")
print(f"{result_4:.2f}%")

