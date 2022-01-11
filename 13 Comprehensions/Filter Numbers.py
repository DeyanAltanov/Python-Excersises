start = int(input())
end = int(input())

filtered_numbers = [num for num in range(start, end + 1) if any([num % number == 0 for number in range(2, 11)])]

print(filtered_numbers)