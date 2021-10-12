def solve(A):
    ret = 0
    #일단 제자리는 다 더해버린다 n번의 연산
    for i in range(len(A)):
        ret += A[i]
    
    #최소값의 index를 찾는 과정 n번의 연산
    minIdx = A.index(min(A))

    #연산수 구해보자. 최악의경우로
    for i in range(minIdx):
        for j in range(i+1, minIdx):
            ret+=min(A[i:j+1])

    #minIdx가 포함된 순서쌍들의 갯수를 구해야함.
    
    


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


A = [int(x) for x in input().split()]
print(solve(A))
