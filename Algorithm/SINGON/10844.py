def solution(n):
    dp = [[0]*10 for _ in range(n+1)] # i번째 마지막 숫자가 j인 개수를 dp[i][j]로 정의한다.
    dp[1][1:] = [1]*9 #한자리 숫자는 일의자리가 1~9까지 각각 한 개이기 때문에
    if n ==1:
        return sum(dp[1])
    for i in range(2,n+1): #두자리 수부터 보면
        for j in range(10): #마지막 숫자가 0~9까지 살펴보면
            if j == 0: #i자리 숫자에서 마지막 숫자가 0인 경우 i-1자리 숫자에서 마지막 숫자가 1인 경우의 수와 동일하다.
                dp[i][j] = dp[i-1][j+1]
            elif j==9: #i자리 숫자에서 마지막 숫자가 9인경우 i-1자리 숫자에서 마지막 숫자가 8인 경우의 수와 동일하다.
                dp[i][j] = dp[i-1][j-1]
            else: #나머지 경우는 i-1자리 숫자에서 숫자가 1 커지는 경우와 i-1자리 숫자에서 1이 작아지는 경우가 있다.
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
    return sum(dp[n])%1000000000
if __name__=="__main__":
    N = int(input())
    print(solution(N))
