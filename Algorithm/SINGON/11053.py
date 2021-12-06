import sys
input = sys.stdin.readline
N = int(input())
A = [0] + list(map(int, input().split()))
dp =[0]*10001 #여기서 dp[i]는 i번째 수를 포함하는 최대 길이이다. 따라서 정답은 N번째 수를 굳이 포함할 필요가 없으므로 max(dp)가 될 것이다. 
# 증가수열 최대길이로 만들기
for i in range(1,N+1):
    maximum = 0 #i를 마지막 항으로 하는 최대 길이
    for j in range(i):
        if A[j] < A[i]:
            if dp[j] >= maximum:
                maximum = dp[j]
    dp[i] = maximum+1
print(max(dp))
