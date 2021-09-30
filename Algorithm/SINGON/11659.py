import sys
from itertools import accumulate
input = sys.stdin.readline
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(accumulate(A))
B.insert(0,0)
for _ in range(M):
    i, j = map(int,input().split())
    print(B[j]-B[i-1])    
