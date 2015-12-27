
from functools import reduce

maxTestCaseNum = int(input())

for i in range(maxTestCaseNum):
    num = int(input())
    divisors = set(reduce(list.__add__, ([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0)))
    divisors.remove(num)
    isWeird = True
    while num <= sum(divisors):
        if num <= 0:
            break
        else:
            num = num - divisors.pop()

        if num in divisors:
            isWeird = False
            break

    print('weird' if isWeird else 'not weird')

