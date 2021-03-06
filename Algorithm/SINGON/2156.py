n = int(input())
A = [0]+[int(input()) for _ in range(n)]
dp = [0]*(10001) #dp[i]는 i개의 포도주 잔이 있을 때 마실 수 있는 포도주의 최대 양
dp[1] = A[1]
if n>=2:
    dp[2] = A[1] + A[2]
if n>=3:
    for i in range(3,n+1):
        dp[i] = max(dp[i-3]+A[i-1]+A[i], dp[i-2]+A[i],dp[i-1]) #i-2번째 최댓값에서 i번째 포도주 잔의 양을 더한 것을 비교하는 것은 당연하고 i-1번째 최댓값이 i-2번째 포도주잔과 i-1번째 포도주 잔을 포함하느냐 안하느냐에 따라 i번째 포도주 잔을 더할 수 있고 없고가 결정되므로 dp[i-3]+A[i-1]+A[i]를 추가적으로 비교해준다.
print(dp[n])

