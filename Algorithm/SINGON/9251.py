X = str(input())
Y = str(input())
dp = [[0]*(len(Y)+1) for _ in range(len(X)+1)] #2차원 행렬로 만들어 최대 개수를 구할 것이다.
for i in range(1, len(X)+1):
    for j in range(1, len(Y)+1):
        if X[i-1] == Y[j-1] : #dp는 첫번째 항이 아무 의미가 없지만 문자열은 첫번째 항부터(X[0], Y[0]) 시작이다.
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
