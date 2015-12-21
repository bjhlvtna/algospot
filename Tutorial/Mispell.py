
maxTestCaseNum = input()

testCase = []
for i in range(int(maxTestCaseNum)):
    testCase.append(input())

for index, case in enumerate(testCase):
    inputData = case.split()
    word = inputData[1]
    print(str(int(index)+1) + ' ' + word[:int(inputData[0])-1]+word[int(inputData[0]):])

