n, L, k = map(int, input().split())

pos = [0 for _ in range(n)]
id = [0 for _ in range(n)]

out = []

cnt = 0

for i in range(n):
    a, b = map(int, input().split())
    pos[i] = a
    id[i] = b
dir=id[:]


temp = []

####
# print(n, L, k)
# print(pos, id, dir)
i = 0
while True:
    
    if i > n-1 :
        i = 0
        if len(temp) > 0 :
            if len(temp) > 1:
                if id[temp[0]] >= id[temp[1]]:
                    out.append(id[temp[1]])
                    pos.pop(temp[1])
                    id.pop(temp[1])
                    dir.pop(temp[1])
                    out.append(id[temp[0]])
                    pos.pop(temp[0])
                    id.pop(temp[0])
                    dir.pop(temp[0])
                else:
                    out.append(id[temp[0]])
                    pos.pop(temp[0])
                    id.pop(temp[0])
                    dir.pop(temp[0])
                    out.append(id[temp[1]])
                    pos.pop(temp[1])
                    id.pop(temp[1])
                    dir.pop(temp[1])
                n-=1
            else:
                out.append(id[temp[0]])
                pos.pop(temp[0])
                id.pop(temp[0])
                dir.pop(temp[0])
        
            n -= 1
        temp.clear()

    if len(out) >= k:
        break

    if dir[i] < 0:
        pos[i] -= 1

        for q in range(n):
            if pos[q] == pos[i] and q != i:
                pos[i] += 2
                dir[i] *= -1
                dir[q] *= -1

        if pos[i] < 0:
            cnt+=1
            temp.append(i)
            # out.append(id[i])
            # pos.pop(i)
            # id.pop(i)
            # dir.pop(i)
            # n -= 1

    elif dir[i] > 0:
        pos[i] += 1

        for q in range(n):
            if pos[q] == pos[i] and q != i:
                pos[i] -= 2
                dir[i] *= -1
                dir[q] *= -1

        if pos[i] > L:
            cnt+=1
            temp.append(i)
            # out.append(id[i])
            # pos.pop(i)
            # id.pop(i)
            # dir.pop(i)
            # n -= 1

    


    i += 1

            
print(out[k-1])
# print(out)

## 백업


# n, L, k = map(int, input().split())

# pos = [0 for _ in range(n)]
# id = [0 for _ in range(n)]

# out = []

# cnt = 0

# for i in range(n):
#     a, b = map(int, input().split())
#     pos[i] = a
#     id[i] = b
# dir=id[:]


# temp = []

# ####
# # print(n, L, k)
# # print(pos, id, dir)
# i = 0
# while True:
#     temp.clear()
#     if i > n-1 :
#         i = 0

#     if len(out) >= k:
#         break

#     if dir[i] < 0:
#         pos[i] -= 1

#         for q in range(n):
#             if pos[q] == pos[i] and q != i:
#                 pos[i] += 2
#                 dir[i] *= -1
#                 dir[q] *= -1

#         if pos[i] < 0:
#             cnt+=1
#             temp.append(i)
#             # out.append(id[i])
#             # pos.pop(i)
#             # id.pop(i)
#             # dir.pop(i)
#             # n -= 1

#     elif dir[i] > 0:
#         pos[i] += 1

#         for q in range(n):
#             if pos[q] == pos[i] and q != i:
#                 pos[i] -= 2
#                 dir[i] *= -1
#                 dir[q] *= -1

#         if pos[i] > L:
#             cnt+=1
#             temp.append(i)
#             # out.append(id[i])
#             # pos.pop(i)
#             # id.pop(i)
#             # dir.pop(i)
#             # n -= 1

#     if len(temp) > 0 :
#         if len(temp) > 1:
#             if id[temp[0]] >= id[temp[1]]:
#                 out.append(id[temp[1]])
#                 pos.pop(temp[1])
#                 id.pop(temp[1])
#                 dir.pop(temp[1])
#                 out.append(id[temp[0]])
#                 pos.pop(temp[0])
#                 id.pop(temp[0])
#                 dir.pop(temp[0])
#             else:
#                 out.append(id[temp[0]])
#                 pos.pop(temp[0])
#                 id.pop(temp[0])
#                 dir.pop(temp[0])
#                 out.append(id[temp[1]])
#                 pos.pop(temp[1])
#                 id.pop(temp[1])
#                 dir.pop(temp[1])
#             n-=1
#         else:
#             out.append(id[temp[0]])
#             pos.pop(temp[0])
#             id.pop(temp[0])
#             dir.pop(temp[0])
        
#         n -= 1


#     i += 1

            
# print(out[k-1])
# # print(out)