n = int(input())
digit_1 = 0
digit_2 = 0
pair = 0
pair_1 = 0
pair_2 = 0
max_difference = 0
counter_pair_1 = 0
counter_pair_2 = 0
for number in range(1, 2 * n + 1):
    value = int(input())
    pair += value
    counter_pair_1 += 1
    counter_pair_2 += 1
    if counter_pair_1 == 2:
        pair_1 = pair
        pair = 0
        counter_pair_2 = 0
    elif counter_pair_2 == 2:
        pair_2 = pair
        pair = 0
        counter_pair_1 = 0
difference = abs(pair_2 - pair_1)
if difference > max_difference:
    max_difference = difference
if difference == 0 or n == 1:
    print(f"Yes, value={pair_1}")
else:
    print(f"No, maxdiff={max_difference}")
