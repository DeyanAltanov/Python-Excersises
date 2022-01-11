def negatives_positives(numbers):
    sums = []
    positives_sum = sum(filter(lambda x: x > 0, numbers))
    negatives_sum = sum(filter(lambda x: x < 0, numbers))
    sums.append(positives_sum)
    sums.append(negatives_sum)
    return sums


numbers = [int(number) for number in input().split()]
sums = negatives_positives(numbers)

print(sums[1])
print(sums[0])
if sums[0] > abs(sums[1]):
    print(f"The positives are stronger than the negatives")
elif sums[0] < abs(sums[1]):
    print(f"The negatives are stronger than the positives")