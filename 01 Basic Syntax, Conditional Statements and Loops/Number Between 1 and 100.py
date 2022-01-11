n = 0

while n < 1 or n > 100:
    n = float(input())

    if 1 <= n <= 100:
        print(f"The number {n} is between 1 and 100")
        break