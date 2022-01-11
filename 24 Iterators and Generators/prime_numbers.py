def get_primes(numbers):
    for number in numbers:
        prime = True
        for num in range(2, number):
            if number % num == 0:
                prime = False
                break
        if number < 2:
            prime = False
        if prime:
            yield number