'''
https://www.acmicpc.net/problem/2012
등수 매기기
[풀이]
1. 참가자들의 예측 등수를 오름차순으로 정렬한다. (등수 자체는 우수한 성적부터 정렬된다)
2. 이 순서로 1, 2, 3, ... 등을 부여해서 이 차이를 구한다.
3. (핵심) 자신보다 예측 등수가 낮은 사람한테 높은 등수를 주지만 않으면 어떻게 나눠줘도 똑같다.
=> 여기서 등수가 높다라는 말은, "순위가 높다" 라는 뜻이 아니라 "숫자가 높다"의 뜻이다.
=> "차이"라는 선형 연산이 이루어지는 것이 첫번째 이유이고,
=> "전체 차이의 합"이 최소라고 하면, 선형 연산에서 이 전체합은 유지되는 것이 두번째 이유이다.
'''
import sys
input = sys.stdin.readline

N = int(input())
preds = sorted([int(input()) for _ in range(N)])
print(sum([abs(prize-pred) for prize, pred in zip(range(1, N+1), preds)]))
