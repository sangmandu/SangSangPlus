import sys
from itertools import accumulate
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(accumulate(list(map(int,input().split()))))
B = [0]*N #N번째 인덱스는 N-K+1부터 N까지 합
target = -100*K #타겟: 최고점
for i in range(N):
    if i<K-1: #누적 합 성립이 안됨
        B[i] = -100*K # 가능한 최저점 이하의 수 아무거나 넣으면 됨.
    elif i== K-1:
        B[i] = A[i] # 누적합에서 빼주는 숫자 없음
    else:
        B[i] = A[i] - A[i-K]
    if target < B[i]:
        target = B[i] #최고점은 타겟을 찍어놔야함.
print(target)
