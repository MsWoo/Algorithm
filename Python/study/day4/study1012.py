def solve(L, S):
	# code here
	count = 0
	
	nums = [0 for _ in range(L)]
	
	nums[0] = 1

	#------------------

	nums2 = nums[:]
	for i in range(len(nums2)):
		nums2[i] = 9
	nums2 = map(str, nums2)
	inputNum = int(''.join(nums2))

	aSum = 0

	limit = 10 ** (L-1)

	while inputNum >= limit:
		inputNum2 = inputNum
		aSum = 0

		while inputNum2 > 0:
			aSum += inputNum2 % 10
			inputNum2 //= 10
		if aSum == S:
			count += 1

		inputNum -= 1

	#-------------------


	# e = 1
	# c = 0
	
	# while True:
		
	# 	# c+=1
		
	# 	if nums[0] == 10 :
	# 		break
			
	# 	if S < 10 and nums[0] == S:
	# 		count+=1
	# 		break
			
		
	# 	else:
	# 		if sum(nums) == S:
	# 			count += 1
				
	# 		nums[-1] += 1
			
			
			
	# 		# for e in range(1, L):
	# 		# 	if (c % (10 ** e) == 0):
	# 		# 		nums[-e] = 0
	# 		# 		nums[-(e+1)] += 1

	# 		for idx in range(L-1,0,-1):
	# 			if nums[idx] == 10:
	# 				nums[idx] = 0
	# 				nums[idx-1] += 1

	return count

L, S = [int(x) for x in input().split()]
print(solve(L, S)%2147483647)