import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = [(0,0)]+list(tuple(map(int, input().split()))for _ in range(N))
dp = [[0]*(K+1) for _ in range(N+1)] #가방수x무게로 행렬을 만듦

for i in range(1, N+1):
    for j in range(1,K+1):
        if j < A[i][0]: #무게 한계가 j일 때 i번째 무게가 이미 한도초과이므로
            dp[i][j] = dp[i-1][j] #이전 것들을 사용해서 최댓값을 구한다.
        else: #조건만 주어진다면 충분히 넣을 수 있다면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i][0]]+A[i][1]) #i번째를 안넣었을 때 무게한계j인 최댓값vs i번째 안넣고 무게한계가 (j-i번째 무게)일 때 최댓값+i번째 무게의 최댓값 을 비교.
print(dp[N][K])
