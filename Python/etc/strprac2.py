n, k, T = input().split()
n = int(n)
k = int(k)-1
data = [input() for _ in range(n)]

ans=[]

for d in data:
    if T in d:
        ans.append(d)
ans.sort()
print(ans[k])