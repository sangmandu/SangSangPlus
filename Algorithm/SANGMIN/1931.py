'''
https://www.acmicpc.net/problem/1931
회의실 배정
[풀이]
1. 핵심은, 회의를 많이해야 한다는 것.
=> 많이 하려면 이전 회의가 빨리 끝내야 또 바로 다음 회의도 빨리 끝나야 될 것이다.
2. 회의가 끝나는 순으로 정렬한다.
=> 회의가 끝나는 시간이 빠른 것들을 고르다보면 많은 회의를 진행할 수 있을 것이다.
=> 끝나는 시간이 같다면 빨리 시작하는 순으로 정렬해야 한다.
=> 왜? 회의의 시작시간과 끝나는 시간이 같을 수도있다.
=> (0, 0) 과 (1, 0)에 대해서 순서에 따라 카운트가 달라질 수 있다.
'''
import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
prior = answer = 0
for st, ed in sorted(meetings, key=lambda x: (x[1], x[0])):
    if prior > st:
        continue
    prior = ed
    answer += 1
print(answer)
