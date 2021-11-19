import sys

n = int(input())
nums = list(map(int, input().split()))

#idx 0 : + / 1 : - / 2 : *
operator_cnt = list(map(int, input().split()))
operator = []
operatorNums = 3

minVal = sys.maxsize
maxVal = -sys.maxsize


def calcul():
    val = nums[0]

    for i, oper in enumerate(operator):
        if oper == 0:
            val += nums[i+1]
        elif oper == 1:
            val -= nums[i+1]
        else:
            val *= nums[i+1]

    return val

def simu(cnt):
    global minVal, maxVal

    if cnt == n-1:
        val = calcul()
        minVal = min(minVal, val)
        maxVal = max(maxVal, val)
        return

    for i in range(operatorNums):
        if operator_cnt[i]:
            operator.append(i)
            operator_cnt[i] -= 1
            simu(cnt + 1)
            operator.pop()
            operator_cnt[i] += 1

simu(0)
print(minVal, maxVal)