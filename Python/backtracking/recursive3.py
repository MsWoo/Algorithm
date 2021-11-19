n, m = map(int, input().split())

ans = []
answer = []

def choose(cnt):
    if cnt == m:
        if sorted(ans) not in answer:
            answer.append(sorted(ans))
        return

    for i in range(1, n+1):
        if i in ans:
            continue
        ans.append(i)
        choose(cnt+1)
        ans.pop()

choose(0)

for a in answer:
    for i in range(len(a)):
        print(a[i], end=" ")
    print()