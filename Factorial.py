number = 5

def factorial(n):
    if n == 0:
        return 1

    i = 0
    f = 1
    while i < n:
        i += 1
        f = f*i
    return f

print(f'Factorial of the number {number}: {factorial(number)}')
