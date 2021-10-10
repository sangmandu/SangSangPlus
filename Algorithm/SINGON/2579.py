import sys
input =  sys.stdin.readline
n = int(input())
scores = [0]+[int(input()) for _ in range(n)] #각 계단별 점수. 시작점은 0점으로 가정
dp = [[scores[0],scores[0]]] #처음 시작점 점수
dp.append([scores[1], scores[1]]) #첫 번째 계단을 지날 때 점수
if n>1:
    dp.append([max(dp[0])+scores[2],dp[1][0]+scores[2]]) # 두 번째 계단부터는 시작점에서 온 경우, 첫 번째 계단을 지나고 온 경우로 나뉜다.
if n>2:
    dp.append([max(dp[1])+scores[3], dp[2][0]+scores[3]]) #세 번째 계단은 첫 번째 계단에서 온경우 첫 번째 계단을 뛰어넘어 두 번째 계단을 온 경우로 나뉜다.
if n>3:
    for i in range(4,n+1):
        dp.append([max(dp[i-2])+scores[i], dp[i-1][0]+scores[i]]) #i 번째에는 i-2번째 계단까지 온 경우의 최댓값에서 i번째 계단 점수를 더하는 경우와 i-2번째 계단을 뛰어넘어 i-1번째 계단을 밟고 온 경우로 나뉘게 된다.
print(max(dp[n]))
