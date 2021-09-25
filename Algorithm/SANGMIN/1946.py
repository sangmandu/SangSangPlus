'''
https://www.acmicpc.net/problem/1946
신입 사원
[풀이]
1. 총 사원수가 10만명이므로 O(n logn)으로 풀어야 하는 문제
=> 이진탐색 또는 힙 예상할 수 있음
2. heapify로 employee를 정렬
=> 이 때 서류 전형 성적으로 정렬이 된다.
=> 서류 전형 순위가 높은(=1에 가까운) 값부터 얻을 수 있음
3. 생각해보자. 이미 서류 전형으로 순위가 정렬된 애들이 이번 시험에 합격하려면 어떻게 해야 할까?
=> 앞사람들의 면접 성적보다 높으면 되지 않을까?
4. 앞사람들의 면접 성적 중에서 max 값을 계속 갱신한다.
=> 앞사람의 best 면접 성적보다도 낮으면 불합격!
'''
import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    employee = [tuple(map(int, input().split())) for _ in range(int(input()))]
    heapify(employee)

    answer, cut = 0, len(employee)
    while employee:
        _, view = heappop(employee)
        if cut < view:
            continue
        answer += 1
        cut = view
    print(answer)





