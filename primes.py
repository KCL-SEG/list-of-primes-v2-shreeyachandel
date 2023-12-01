"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(num):
    if num<2:
        return False
    for i in range (2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError("Number of primes must be positive")

    list = []
    num = 2
    while len(list) < number_of_primes:
        if is_prime(num):
            list.append(num)
        num +=1
    
    return list
