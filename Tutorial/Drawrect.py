

maxTestCaseNum = input()

testCase = []
for i in range(int(maxTestCaseNum)):
    case = []
    for j in range(3):
        case.append(input().split(' '))
    testCase.append(zip(case[0], case[1], case[2]))

for case in testCase:
    result = []
    for axis in case:
        minimum = min(axis)
        maximum = max(axis)
        minCount = axis.count(minimum)
        result.append(maximum if minCount == 2 else minimum)
    print(result[0] + ' ' + result[1])




