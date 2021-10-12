def solve(L, S):
	# code here
	count = 0
	
	nums = [0 for _ in range(L)]
	
	nums[0] = 1

	# e = 1
	# c = 0
	
	while True:
		
		# c+=1
		
		if nums[0] == 10 :
			break
			
		if S < 10 and nums[0] == S:
			count+=1
			break
			
		
		else:
			if sum(nums) == S:
				count += 1
				
			nums[-1] += 1
			
			
			
			# for e in range(1, L):
			# 	if (c % (10 ** e) == 0):
			# 		nums[-e] = 0
			# 		nums[-(e+1)] += 1

			for idx in range(L-1,0,-1):
				if nums[idx] == 10:
					nums[idx] = 0
					nums[idx-1] += 1

	return count

L, S = [int(x) for x in input().split()]
print(solve(L, S)%2147483647)