
maxTestCaseNum = input()

testCase = []
for i in range(int(maxTestCaseNum)):
    testCase.append(input())

for case in testCase:
    print(case[::2]+case[1::2])


