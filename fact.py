n=int(input('Enter a number: '))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
a=factorial(n)
print(f'The factorial of {n} is {factorial(n)}')