k, n = map(int, input().split())

ans = []

def printArray():
    for a in ans:
        print(a, end=" ")
    print()

def choose(cnt):
    if cnt == n:
        printArray()
        return
    
    for i in range(1, k+1):
        ans.append(i)
        choose(cnt + 1)
        ans.pop()

choose(0)