
from functools import reduce


def make_divisors(num):
    return set(reduce(list.__add__, ([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0)))

# canMake(i, j) => (j == 0 or canMake(i-1, j) or canMake(i-1, j-divisors[i-1]))
# a. j = 0 이라면, i개에서 한 개도 안 고르면 되니까 ok입니다.
# b. 만약 i개중에 마지막 숫자를 빼 놓고, 첫 i-1 개만으로도 j 를 만들 수 있다면 ok 입니다.
# c. i개 중에 마지막 숫자를 사용한다고 보고, 나머지 i-1 개로 j-divisors[i-1] 을 만들 수 있다면 ok 입니다.
# 이 점화식을 구현하면 됩니다.


def is_weird(divisor_cnt, compared_num):

    if divisor_cnt == 1:
        return True

    if is_weird(divisor_cnt-1, compared_num - divisors[divisor_cnt]):
        for x in range(divisor_cnt):
            for y in range(divisor_cnt):
                if x == y:
                    continue
                sum_result = 0
                if subSetSum[x+y] == 0:
                    subSetSum[x+y] = divisors[x] + divisors[y]

                sum_result += subSetSum[x+y]

                if sum_result == compared_num:
                    return False
        return True
    else:
        return False


divisors = make_divisors(12)

subSetSum = [-1]*500001

# is_weird(len(divisors), 12)
subSetSum[50000] = 1
print(len(subSetSum))
print(subSetSum[50000])
# for i in subSetSum:
#     print(i)
