A = [int(x) for x in input().split()]

n = A[0]
e = 0
ret = 0

def access(idx):
    global n,e,ret

    if idx >= len(A):
        return False
    if idx == len(A)-1:
        ret += 1
        return True
    if A[idx] == 0:
        return False
    if A[A[idx]+idx] > 1:
        e = idx+A[idx] 
        n = e + A[e]
    access(idx+A[idx])

while n > e:
    access(n)
    if ret >= 1:
        break
    n-=1
print("True" if ret >= 1 else "False")