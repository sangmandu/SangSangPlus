'''
https://www.acmicpc.net/problem/2565
전깃줄
[풀이]
1. 전깃줄 정보를 start position을 기준으로 오름차순 정렬한다.
=> 따라서, 두 전깃줄 정보를 비교할 때는 두 전깃줄의 인덱스가 알면 end position만 비교할 수 있다.
2. 이전 전깃줄보다 end pos가 높으면 현재의 전깃줄과 겹치지 않는다
=> 따라서, 이전 전깃줄보다 +1 되는 겹치지 않는 전깃줄 수를 가질 수 있다
=> 또는, 이미 겹치지 않는 전깃줄 수가 현재가 더 많이 가지고 있다면 그대로 가진다.
3. 전체 전깃줄 수에서 겹치지 안흔 전깃줄 수를 뺸다.
'''
import sys
input = sys.stdin.readline

n = int(input())
lst = sorted([tuple(map(int, input().split())) for _ in range(n)])
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if lst[j][1] < lst[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))
