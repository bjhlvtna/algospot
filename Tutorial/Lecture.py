

maxTestCaseNum = input()

testCase = []
for i in range(int(maxTestCaseNum)):
    testCase.append(input())


nLetter = 2
for case in testCase:
    splitString = [case[i:i+nLetter] for i in range(0, len(case), nLetter)]
    splitString.sort()
    print(''.join(splitString))



