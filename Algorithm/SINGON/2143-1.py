import sys
from itertools import accumulate
input = sys.stdin.readline
T = int(input())
n = int(input())
A = [0]+list(accumulate(list(map(int, input().split()))))
m = int(input())
B = [0]+list(accumulate(list(map(int, input().split()))))
C = dict()
cnt = 0
for i in range(1,len(A)):
    for j in range(i,len(A),1):
        c = A[j]-A[i-1]
        if str(c) not in C.keys():
            C[str(c)] =1
        else:
            C[str(c)] +=1
for i in range(1,len(B)):
    for j in range(i, len(B),1):
        if str(T-(B[j]-B[i-1])) in C.keys():
            cnt += C[str(T-(B[j]-B[i-1]))]
print(cnt)
