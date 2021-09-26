'''
https://www.acmicpc.net/problem/11000
강의실 배정
[풀이]
1. 먼저 시작하는 수업부터 강의실을 채운다.
=> 이 때 '채운다는' 의미는 끝나는 시간을 추가한다는 뜻
2. 이 추가한 시간이 오름차순 정렬 될 수 있도록 heap을 사용한다
3. heap에서 나오는 시간은 끝나는 시간이 가장 작은 시간인데 이 보다도 크면 강의실을 하나 더 쓸 수 밖에 없다.
'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
cls = sorted([list(map(int, input().split())) for _ in range(n)])
end, ans = [cls[0][1]], 1
for s, t in cls[1:]:
    if end[0] <= s:
        heappop(end)
    heappush(end, t)
    ans = max(ans, len(end))
print(ans)

