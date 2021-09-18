A = [int(x) for x in input().split()]
sum = 0
A = sorted(A)

if len(A) % 2 == 1:
    idx = (len(A)-1) // 2
    for i in range(idx):
        sum += A[idx] - A[i]
    for i in range(len(A)-1,idx,-1):
        sum += A[i] - A[idx]

else:
    idx = len(A) // 2
    for i in range(idx):
        sum += A[idx] - A[i]
    for i in range(len(A)-1,idx,-1):
        sum += A[i] - A[idx]

print(sum)