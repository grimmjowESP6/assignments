n = int(input('Enter a number: '))
def fact(a):
    if a < 2:
        return 1
    else:
        return a * fact(a-1)
result = fact(n)
print(result)