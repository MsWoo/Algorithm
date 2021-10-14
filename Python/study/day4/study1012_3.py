def fact(n):
    if n<=1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result
def ncr(n, r):
    return fact(n)//(fact(r)*fact(n-r))


# def checkAndSum():
#     global ret

#     #최소값의 index를 찾는 과정 n번의 연산
#     minIdx = A.index(min(A))
#     minV = min(A)

#     for pair in pairs:
#         i, j = pair
#         if i <= minIdx <= j:
#             ret += minV
#         else:
#             ret += min(A[i:j+1])

def solve(A):
    global ret
    #일단 제자리는 다 더해버린다 n번의 연산
    for i in range(len(A)):
        ret += A[i]

    pairCount = ncr(len(A), 2)
    # print(pairCount)
    minIdx = A.index(min(A))
    minV = min(A)

    for i in range(minIdx-1):
        for j in range(i+1, minIdx):
            pairCount -= 1
            ret += min(A[i:j+1])
    
    for i in range(minIdx+1, len(A)-1):
        for j in range(i+1, len(A)):
            pairCount -= 1
            ret += min(A[i:j+1])

    
    # print(ret, minV, pairCount)

    ret += minV * pairCount



    # for i in range(len(A)-1):
    #     for j in range(i+1, len(A)):
    #         pairs.append((i,j))

    # checkAndSum()


    #연산수 구해보자. 최악의경우로
    # for i in range(minIdx):
    #     for j in range(i+1, minIdx):
    #         ret+=min(A[i:j+1])

    #minIdx가 포함된 순서쌍들의 갯수를 구해야함.
    return ret
    


	# O(n^2)으로 풀이했더니 timeout뜬다 효율성 증가시키자.-----
    # temp = []
    # ret = 0

    # for i in range(len(A)):
    #     for j in range(i, len(A)):
    #         if i == j:
    #             ret += A[i]
    #         else:
    #             ret += min(A[i:j+1])
    # return ret
    #-------------

ret = 0
pairs = []

A = [int(x) for x in input().split()]
print(solve(A))
