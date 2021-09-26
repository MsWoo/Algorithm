n = [int(x) for x in input().split()]
n=sorted(n)

maj = -1
prev = n[0]
cnt = 1

for i in range(1, len(n)):
    if prev == n[i]:
        prev = n[i]
        cnt+=1
    else:
        prev = n[i]
        cnt=1

    if cnt > len(n)//2:
        maj = prev
        break

print(maj)