import sys
'''
정렬후 heap을 이용하여 카드 합체 놀이를 해결하였습니다.
heap 구조의 트리를 이용하면(만약 최소 힙이라면) 항상 첫번째 index는 최솟값이 되므로 
해당 문제를 해결하기 적합하다고 판단하였고 파이썬의 heapq는 최소 힙 방식이라서 heapq 모듈
을 사용하여 해결하였습니다.
'''
import heapq

input = sys.stdin.readline

def solve(n ,m):
    card_list = list(map(int, input().split()))
    card_list.sort() 

    for i in range(m):
        result = heapq.heappop(card_list)
        target = heapq.heappop(card_list)
        result += target
        heapq.heappush(card_list, result)
        heapq.heappush(card_list, result)

    print(sum(card_list))


if __name__ == '__main__':
    n, m = map(int, input().split())
    solve(n, m)