import sys
input = sys.stdin.readline
from itertools import accumulate #시간 단축을 위해 accumulate 사용
r, c, q = map(int, input().split())
dp = [[0]*c]
for _ in range(r):
    a= [0] + list(map(int, input().split()))
    b = list(accumulate(a))
    dp.append(b)
for _ in range(q):
    a1, b1, a2, b2 = map(int, input().split())
    answer = 0
    for i in range(a1, a2+1):
        answer += dp[i][b2] - dp[i][b1-1]
    print(answer//((a2-a1+1)*(b2-b1+1)))