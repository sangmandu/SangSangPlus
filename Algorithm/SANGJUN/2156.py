from sys import stdin
input = stdin.readline

 # 연속해서 포도주를 세 번 마실 수 없으므로 현재 잔을 기준으로 가능한 경우의 수는 다음과 같다.
 # dp[i - 3]까지는 모두 공통. dp[i - 3]일 때 마지막 잔을 마셨는지 마시지 않았는지 모름.
 # oox : dp[i - 3]의 상태를 모르기 때문에 이전의 두 잔을 모두 마시는 경우의 최대값은 dp[i - 1]
 # oxo : 위와 마찬가지로 전전 잔을 마시고 현재잔을 마시는 경우의 최대값은 dp[i - 2] + wine[i]
 # xoo : dp[i - 3] + wine[i - 1] + wine[i - 2]
 
def _2156(n : int, wine : list):
    dp = [0] * n
    
    if n >= 1:
        dp[0] = wine[0]
    if n >= 2:
        dp[1] = wine[0] + wine[1]
    
    if n >= 3:
        dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])

        for i in range(3, n):
            dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i], dp[i - 1])

    return dp[n - 1]

    # https://zoonvivor.tistory.com/133

if __name__ == "__main__":
    n = int(input())
    wine = [int(input()) for _ in range(n)]
    print(_2156(n, wine))
