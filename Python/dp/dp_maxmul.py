#최대곱구간
A = list(map(int, input().split()))

dp_plus = [1 for _ in range(len(A))]
dp_minus = [1 for _ in range(len(A))]

dp_plus[0] = A[0]
dp_minus[0] = A[0]

for i in range(1,len(A)):
    dp_plus[i] = max(A[i], max(dp_plus[i-1]*A[i], dp_minus[i-1]*A[i]))
    dp_minus[i] = min(A[i], min(dp_plus[i-1]*A[i], dp_minus[i-1]*A[i]))

print(max(dp_plus))