n = int(input())
guest = list(map(int, input().split()))
a, b = map(int, input().split())

ans = 0

for g in guest:
    if (g-a) > 0:
        if (g-a) % b == 0 :
            ans += (g-a)//b
        else:
            ans += (g-a)//b+1 

ans += n

print(ans)