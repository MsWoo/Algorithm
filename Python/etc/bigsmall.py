def solve(A):
    temp = sorted(A)
    ret = []
    while len(temp) > 0:
        ret.append(temp[0])
        temp.pop(0)
        if len(temp) > 0:
            ret.append(temp.pop())
    return ret

def check(B):
    if not (B[0] <= B[1]): return False
    for i in range(1, len(B)-1):
        if i%2 == 1 and not (B[i] >= B[i+1]):
            return False
        if i%2 == 0 and not (B[i] <= B[i+1]):
            return False
    return True

A = [int(x) for x in input().split()]
B = solve(A)
print(check(B))
