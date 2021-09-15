'''
https://www.acmicpc.net/problem/1007
벡터 매칭
[풀이]
1. 짝수인 m개를 입력 받을 때 m=2n 이라하면, 벡터의 합은 n개는 더해지고 n개는 뺴진다.
=> 벡터는 (x1-x2, y1-y2) 처럼 임의의 두 점의 차로 이루어지기 때문이다. 
2. 모든 점의 합을 구한다.
=> (x1+x2+x3+..., y1+y2+y3+...)
3. combinations을 통해 절반의 좌표를 구한다.
=> 이 때, 절반의 좌표가 결정되면 자동으로 나머지 절반의 좌표가 결정된다.
=> 따라서 combinations 결과의 절반은 사용하지 않아도 된다.
4. 이후 절반의 좌표는 2배를 해서 뺀다. 2배를 해야 우리가 원하던 벡터의 합 모양이 된다.
5. 구한 벡터의 합을 계속 비교한다.
'''
import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    point = [list(map(int, input().split())) for _ in range(N)]
    sum_x, sum_y = map(sum, zip(*point))

    min_dist = 4e+5
    cases = list(combinations(list(range(N)), N // 2))
    for c in cases[:len(cases)//2]:
        part_x, part_y = map(sum, zip(*[point[idx] for idx in c]))
        x, y = sum_x - 2*part_x, sum_y - 2*part_y
        min_dist = min(min_dist, (x**2 + y**2) ** 0.5)

    print(min_dist)
