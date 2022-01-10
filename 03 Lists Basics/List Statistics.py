n = int(input())

positives_list = []
negatives_list = []
negatives_sum = 0

for i in range(n):
    number = int(input())
    if number >= 0:
        positives_list.append(number)
    else:
        negatives_list.append(number)

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}. Sum of negatives: {sum(negatives_list)}")