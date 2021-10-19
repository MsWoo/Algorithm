n = int(input())
A = list(map(int, input().split()))

com = [0 for _ in range(101)]
cnt = 0

for ele in A:
    if com[ele] == 0:
        com[ele] = 1
    else:
        cnt+=1

print(cnt)
