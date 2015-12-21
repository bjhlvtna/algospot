
maxTestCaseNum = input()

testCase = []
for i in range(int(maxTestCaseNum)):
    testCase.append(input())

for index, case in enumerate(testCase, 1):
    inputData = case.split()
    word = inputData[1]
    print(str(index) + ' ' + word[:int(inputData[0])-1]+word[int(inputData[0]):])

