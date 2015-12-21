
maxTestCaseNum = input()

testCase = []
for i in range(int(maxTestCaseNum)):
    testCase.append(input())

for case in testCase:
    num = int(case)
    divisors = [x for x in range(1, num+1) if num%x == 0]
    divisors.pop()

    for x in range(len(divisors)):
        num = num - divisors.pop()
        if num in divisors:
            print('not weird')
            break

    if len(divisors) == 0:
        print('weird')