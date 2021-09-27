'''
https://www.acmicpc.net/problem/13305
주유소
[풀이]
1. 현재 주유소 가격이 어떻든 다음 주유소 까지 가는 거리만큼은 주유를 해야한다.
2. 다음 주유소가 더 저렴하면 거기서 또 충전을 고려한다.
3. 현재 주유소가 더 저렴하면 다음 주유소에서 다다음 주유소까지의 거리만큼 또 주유한다.
4. 이를 반복한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
min_price, cur_dist = price[0], dist[0]
answer = 0
for d, p in zip(dist[1:], price[1:-1]):
    if p < min_price:
        answer += min_price * cur_dist
        cur_dist = d
        min_price = p
        continue
    cur_dist += d
print(answer + min_price * cur_dist)


