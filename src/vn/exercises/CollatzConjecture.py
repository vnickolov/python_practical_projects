# Collatz Conjecture
# Start with a number n > 1.
# Find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.


def calculate_conjecture(n, step):
    if n == 1:
        return step

    x = n
    if x % 2 == 0:
        x = int(n / 2)
    else:
        x = int(n * 3 + 1)

    return calculate_conjecture(x, step + 1)


def conjecture(n):
    return calculate_conjecture(n, 1)
