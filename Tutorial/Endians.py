

bitMasking = lambda x, y: (x & (0xff << y)) >> y
bitSum = lambda x, y: ((x << 8) | y)
#unsigned32 = lambda x: x & 0xFFFFFFFF

numberCnt = input()
numberList = [];
for i in range(int(numberCnt)):
   numberList.append(input())


for number in numberList:
    result = 0
    masking = 0
    for bit in range(0, 32, 8):
        masking = (bitMasking(int(number), bit))
        result = bitSum(result, masking)
    print(result)



