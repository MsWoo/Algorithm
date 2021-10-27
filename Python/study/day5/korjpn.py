def solve(kor, jpn, k_goals, j_goals):
	# kor[1] ... kor[n], jpn[1] ... jpn[n]
    n = len(kor) - 1

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
	# dp[i][j] = kor[1]...kor[i]와 jpn[1]...jpn[j]에 대한 최대 가능 골 수로 정의
	# dp[n][n]이 우리가 원하는 답

    first, second, third, fouth = 0, 0, 0, 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if kor[i] == 'W' and jpn[j] == 'L':
                if k_goals[i] > j_goals[j]:
                    first = max(first, k_goals[i] + j_goals[j])
                    # print(first)
                pass

            elif kor[i] == 'L' and jpn[j] == 'W':
                if k_goals[i] < j_goals[j]:
                    second = max(second, k_goals[i] + j_goals[j])
                    # print(second)
                pass

			# dp[i][j] = 4가지 경우(first, second, third, fourth)가 가능
			#            그 중에서 최대 골 수를 계산
			# kor[i]와 jpn[j]가 짝을 맺는 경우와 둘 다 고려에서 제외되는 경우
			# kor[i]와 jpn[j] 중 하나만 고려에서 제외되는 경우
			# first, second, third, fouth를 계산해보자
			#
            dp[i][j] = max(first, second, third, fouth)
            
    dp[n][n] = first+second
    return dp[n][n]

# kor = 한국의 W와 L의 문자열, jpn = 일본의 W와 L의 문자열 (주의: kor[1], jpn[1]부터 시작)
kor = ' '+input()
k_goals = [0] + [int(x) for x in input().split()]
jpn = ' '+input()
j_goals = [0] + [int(x) for x in input().split()]

#print(kor, k_goals, jpn, j_goals)

print(solve(kor, jpn, k_goals, j_goals))