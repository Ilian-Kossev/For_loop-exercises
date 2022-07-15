n = int(input())
counter_n1 = 0
counter_n2 = 0
counter_n3 = 0
counter_n4 = 0
counter_n5 = 0
result_1 = 0
result_2 = 0
result_3 = 0
result_4 = 0
result_5 = 0
for number in range(1, n + 1):
    value = int(input())
    if value < 200:
        counter_n1 += 1
        result_1 = counter_n1 / n * 100
    elif 200 <= value < 400:
        counter_n2 += 1
        result_2 = counter_n2 / n * 100
    elif 400 <= value < 600:
        counter_n3 += 1
        result_3 = counter_n3 / n * 100
    elif 600 <= value < 800:
        counter_n4 += 1
        result_4 = counter_n4 / n * 100
    elif value >= 800:
        counter_n5 += 1
        result_5 = counter_n5 / n * 100
print(f"{result_1:.2f}%")
print(f"{result_2:.2f}%")
print(f"{result_3:.2f}%")
print(f"{result_4:.2f}%")
print(f"{result_5:.2f}%")
