n = int(input())
result = 0
total_counter = 0
counter_below_10 = 0
counter_below_20 = 0
counter_below_30 = 0
counter_below_40 = 0
counter_below_50 = 0
counter_invalid_number = 0
for number in range(1, n + 1):
    value = int(input())
    total_counter += 1
    if 0 <= value < 10:
        result += value * 0.2
        counter_below_10 += 1
    elif 10 <= value < 20:
        result += value * 0.3
        counter_below_20 += 1
    elif 20 <= value < 30:
        result += value * 0.4
        counter_below_30 += 1
    elif 30 <= value < 40:
        result += 50
        counter_below_40 += 1
    elif 40 <= value <= 50:
        result += 100
        counter_below_50 += 1
    elif value > 50 or value < 0:
        result /= 2
        counter_invalid_number += 1
percent_below_10 = counter_below_10 / total_counter * 100
percent_below_20 = counter_below_20 / total_counter * 100
percent_below_30 = counter_below_30 / total_counter * 100
percent_below_40 = counter_below_40 / total_counter * 100
percent_below_50 = counter_below_50 / total_counter * 100
percent_invalid_number = counter_invalid_number / total_counter * 100
print(f"{result:.2f}")
print(f"From 0 to 9: {percent_below_10:.2f}%")
print(f"From 10 to 19: {percent_below_20:.2f}%")
print(f"From 20 to 29: {percent_below_30:.2f}%")
print(f"From 30 to 39: {percent_below_40:.2f}%")
print(f"From 40 to 50: {percent_below_50:.2f}%")
print(f"Invalid numbers: {percent_invalid_number:.2f}%")