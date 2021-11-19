import sys

# 입력
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

moning = []
evening = []

ans = sys.maxsize

# 아침에 할 일과 저녁에 할 일의 업무강도를 계산하여 그 차이를 Return
def calcul():
    ret = 0
    ret2 = 0

    for i in range(n//2):
        for j in range(n//2):
            # 순열개념 중복제거
            if j == i:
                continue
            ret += grid[moning[i]][moning[j]]
            ret2 += grid[evening[i]][evening[j]]

    return ret-ret2 if ret>ret2 else ret2-ret

def choose_job():
    global ans

    # 종료조건 : 아침에 할 일이 n//2인 경우
    if len(moning) == (n // 2):
        # 아침 일 제외하고는 모두 저녁 일
        evening.clear()
        for i in range(n):
            if i not in moning:
                evening.append(i)

        # 최소값 비교
        ans = min(ans, calcul())
        return

    for i in range(n):
        # 중복제거
        if i in moning:
            continue
        # 조합개념
        if len(moning) != 0 and moning[-1] > i:
            continue
        moning.append(i)
        choose_job()
        moning.pop()

choose_job()
print(ans)