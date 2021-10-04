'''
https://www.acmicpc.net/problem/3020
개똥벌레
[풀이]
1. 핵심은, 석순과 종유석을 언제 부딪히는지는 상관 없다는 것.
=> 따라서, 석순과 종유석의 인덱스를 유지할 필요가 없다.
=> 정렬을 이용해 풀 수 있음
2. 석순과 종유석이 부딪히는 경우의 수를 따로 구하고 이후에 종합한다.
3. 내가 당장의 최소한의 장애물도 넘지 못하면 이후의 장애물도 넘지 못한다는 원리를 이용
=> 매번 최소 장애물을 비교해서 이보다 작으면 이후의 장애물 개수를 저장
=> 최소 장애물을 넘을 수 있으면 이를 pop하고 다음 장애물과 비교
'''
import sys
input = sys.stdin.readline

from collections import deque
n, h = map(int, input().split())
obt = [int(input()) for idx in range(n)]
bot, top = deque(sorted(obt[::2])), deque(sorted(obt[1::2]))
stair_bot, stair_top = [0]*h, [0]*h

for idx in range(h):
    while bot:
        if idx < bot[0]:
            stair_bot[idx] = len(bot)
            break
        bot.popleft()
    while top:
        if idx < top[0]:
            stair_top[idx] = len(top)
            break
        top.popleft()

lst = [sb+st for sb, st in zip(stair_bot, stair_top[::-1])]
print(min(lst), lst.count(min(lst)))
