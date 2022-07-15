number_students = int(input())
total_score = 0
exam_counter = 0
counter_below_3 = 0
counter_below_4 = 0
counter_below_5 = 0
counter_below_6 = 0
for number in range(1, number_students + 1):
    grade = float(input())
    exam_counter += 1
    total_score += grade
    if 2 <= grade < 3:
        counter_below_3 += 1
    elif 3 <= grade < 4:
        counter_below_4 += 1
    elif 4 <= grade < 5:
        counter_below_5 += 1
    elif 5 <= grade <= 6:
        counter_below_6 += 1
average_score = total_score / exam_counter
percent_below_3 = counter_below_3 / exam_counter * 100
percent_below_4 = counter_below_4 / exam_counter * 100
percent_below_5 = counter_below_5 / exam_counter * 100
percent_below_6 = counter_below_6 / exam_counter * 100
print(f"Top students: {percent_below_6:.2f}%")
print(f"Between 4.00 and 4.99: {percent_below_5:.2f}%")
print(f"Between 3.00 and 3.99: {percent_below_4:.2f}%")
print(f"Fail: {percent_below_3:.2f}%")
print(f"Average: {average_score:.2f}")