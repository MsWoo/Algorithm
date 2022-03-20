n, k = map(int, input().split())

block = [0 for _ in range(n)]

for i in range(k):
    s, e = map(int, input().split())
    for j in range(s-1, e):
        block[j] += 1

block.sort()
print(block[len(block)//2])