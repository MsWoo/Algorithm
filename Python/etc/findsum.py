k = int(input())
n = [int(x) for x in input().split()]
n2 = n[:]

cnt = 0

# for i in range(len(n)-1, -1, -1):
#     t = k - n[i]
#     n2.pop()
#     if t in n2:
#         cnt+=1


for i in range(len(n)):
    t = k-n[i]
    n2.pop(0)
    if t in n2:
        cnt += 1


# for i in range(len(n)-1):
#     for j in range(i+1, len(n)):
#         if n[i]+n[j] == k:
#             cnt+=1

print(cnt)