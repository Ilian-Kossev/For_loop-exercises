stadium_capacity = int(input())
total_number_fans = int(input())
counter_a = 0
counter_b = 0
counter_v = 0
counter_g = 0
for number in range(1, total_number_fans + 1):
    fan = input()
    if fan == "A":
        counter_a += 1
    elif fan == "V":
        counter_v += 1
    elif fan == "B":
        counter_b += 1
    elif fan == "G":
        counter_g += 1
percent_fans_a = counter_a / total_number_fans * 100
percent_fans_b = counter_b / total_number_fans * 100
percent_fans_v = counter_v / total_number_fans * 100
percent_fans_g = counter_g / total_number_fans * 100
percent_all_fans = total_number_fans / stadium_capacity * 100
print(f"{percent_fans_a:.2f}%")
print(f"{percent_fans_b:.2f}%")
print(f"{percent_fans_v:.2f}%")
print(f"{percent_fans_g:.2f}%")
print(f"{percent_all_fans:.2f}%")