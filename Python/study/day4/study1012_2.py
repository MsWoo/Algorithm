def check(A):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            return False
    return True

def getAvr(A):
    ret = 0
    for i in range(len(A)):
        ret += A[i]
    return round(ret/len(A))

#1번 2번만 제출해도 1,2,3,4,10 pass인데 1,2,3번 다 적용해도 그대로다 정답률은.

def solve(A):
	# code here
    if check(A):
        return 0
    
    ret = []

    temp = A[:]

    #2번 평균으로만 구하기 -----
    avr = getAvr(A)
    avrIdx = A.index(avr)
    count = 0
    for i in range(len(A)):

        if i < avrIdx:
            if A[i] > avr:
                count += (A[i] - avr)
        else:
            if A[i] > avr:
                count += (A[i] - avr)
            elif A[i] < avr:
                count += (avr - A[i])
    
    ret.append(count)


    #----------

    #3번평균으로 맞추는 코드 + avrIdx 이후로는 1번기준으로하는것--------------
    A = temp[:]
    count = 0

    avr = getAvr(A)
    avrIdx = A.index(avr)
    std = 0
    for i in range(len(A)-1):

        if i < avrIdx:
            if A[i] > avr:
                count += (A[i] - avr)
        else:
            if A[i] > A[i+1]:
                while True:
                    if A[i] == A[i+1]:
                        break
                    A[i+1] += 1
                    count += 1

        std = A[i]


    ret.append(count)

    #------------

    #1번기준으로 짯던 코드-----
    A = temp[:]
    std = 0
    count = 0

    for i in range(len(A)-1):
        
        if A[i] > A[i+1]:
            #기준보다 크거나 같으면 깎는다.
            if A[i+1] >= std:
                while True:
                    if A[i] == A[i+1]:
                        break
                    A[i] -= 1
                    count += 1
            #기준보다 작으면 올린다.
            else:
                while True:
                    if A[i] == A[i+1]:
                        break
                    A[i+1] += 1
                    count += 1
        #기준은 A[i-1]
        std = A[i]

    ret.append(count)

    return min(ret)
    #----------------

    
            


A = [int(x) for x in input().split()]
print(solve(A))