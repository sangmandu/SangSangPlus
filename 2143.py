import sys
from collections import defaultdict #defaultdict는 내장함수가 아닙니다.
input = sys.stdin.readline
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

dictA = defaultdict(int) # 리스트 A의 i~j의 합을 key, 경우의 수를 value로 잡고자 dictA 생성

cnt = 0 #경우의 수 세기

for i in range(len(A)):
    for j in range(i,len(A),1):
        dictA[sum(A[i:j+1])] +=1
# 현재 리스트 A의 i~j의 합을 key, 경우의 수를 value로 모든 경우의 수를 dictA에 넣음
for i in range(len(B)):
    for j in range(i, len(B),1):
        cnt += dictA[T-sum(B[i:j+1])] # T-sum(B[i:j+1])이 dictA key에 있을 경우 T = A[s]+...A[k]+B[i]+...B[j]로 만들 수 있는 것이다. value 값이 T-(B[i]+...B[j])를 만들 수 있는 경우의 수 이므로 cnt +=dictA[T-sum(B[i:j+1])] 하면 된다.
print(cnt)
