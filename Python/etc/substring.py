n = input()

ans = []
temp = []
idx = []

temp.append(n[0])
idx.append(0)
for i in range(1, len(n)):
    print(temp)
    if n[i] in temp:
        if len(ans) < len(temp):
            ans = idx[:]
        idx.clear()
        temp.clear()

        j = i-1
        while True:
            if n[i] == n[j]:
                break
            idx.insert(0, j)
            temp.insert(0, n[j])
            j -= 1

    idx.append(i)
    temp.append(n[i])
if len(ans) < len(temp):
    ans = idx[:]

print(ans[0], len(ans))
