n = float(input())

if n == 0:
    print("zero")
elif 0 < n < 1:
    print("small positive")
elif 1 <= n <= 1000000:
    print("positive")
elif n > 1000000:
    print("large positive")
elif 0 < abs(n) < 1:
    print("small negative")
elif 1 <= abs(n) <= 1000000:
    print("negative")
elif 1000000 < abs(n):
    print("large negative")