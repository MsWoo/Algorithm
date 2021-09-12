stack = []
stack2 = []

while True:
	n = input()
	a = n[:5]

	if a == "push ":
		num = int(n[5:])
		stack.append(num)
		
		if len(stack2) == 0 :
			stack2.append(num)
		else:
			temp = stack2.pop()
			if temp >= num:
				stack2.append(temp)
			else:
				stack2.append(temp)
				stack2.append(num)

		
	elif a == "max":
		if len(stack) == 0:
			print("EMPTY")
		else:
			print(stack2[-1])
	
	elif a == "pop":
		if len(stack) == 0:
			print("EMPTY")
		else:
			if stack[-1] == stack2[-1]:
				stack2.pop()
			print(stack.pop())

	elif n == "exit":
		break