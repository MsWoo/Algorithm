n = input()

hc = 0
sc = 0

while True:
    if ":-)" not in n and ":-(" not in n:
        break
    else:
        if ":-)" in n:
            hc+=1
            n = n.replace(":-)", "", 1)
        if ":-(" in n:
            sc+=1
            n = n.replace(":-(", "", 1)


if hc == 0 and sc == 0 :
    print("none")
elif hc == sc:
    print("unsure")
else:
    print("happy" if hc > sc else "sad")
