fir = []
sec = []

while True:
    n = input()
    a = n[:4]

    if a == "enq ":
        num = int(n[4:])
        fir.append(num)
        #print(fir)

    elif a == "deq":
        if len(sec) == 0:
            for _ in range(len(fir)):
                sec.append(fir.pop())
                #print(sec)
        if len(fir) == 0 and len(sec) == 0:
            print("EMPTY")
        else:
            print(sec.pop())

    elif n == "exit":
        break

