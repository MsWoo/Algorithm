n = int(input())

star = 2*n-1
empty = n-1
t = 1
flag = 0

for _ in range(star):
    for _ in range(empty):
        print(" ", end="")

    for _ in range(t):
        print("*", end="")

    for _ in range(empty):
        print(" ", end="")

    print()

    if t == star:
        flag = 1

    if flag == 1:
        t -= 2
        empty += 1
    else:
        t += 2
        empty -= 1