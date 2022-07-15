from sys import maxsize

n = int(input())
min_num_even = maxsize
max_num_even = -maxsize
min_num_odd = maxsize
max_num_odd = -maxsize
sum_value_even = 0
sum_value_odd = 0
for number in range(1, n + 1):
    value = float(input())
    if number % 2 == 0:
        sum_value_even += value
        if value < min_num_even:
            min_num_even = value
        if value > max_num_even:
            max_num_even = value
    else:
        sum_value_odd += value
        if value < min_num_odd:
            min_num_odd = value
        if value > max_num_odd:
            max_num_odd = value
print(f"OddSum={sum_value_odd:.2f},")
if min_num_odd == maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={min_num_odd:.2f},")
if max_num_odd == -maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={max_num_odd:.2f},")

print(f"EvenSum={sum_value_even:.2f},")
if min_num_even == maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={min_num_even:.2f},")
if max_num_even == -maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={max_num_even:.2f}")

