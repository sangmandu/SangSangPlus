import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split())) #Ai 값 모음
dp = [0]*(N+1)
for i in range(1,N+1):
    dp[i] = dp[i-1]+A[i-1] #1차원에서의 dp
M = int(input())
for _ in range(M):
    i, j = map(int,input().split())
    print(dp[j]-dp[i-1])
# 느낀점 : Sum이라는 함수보다 dp를 이용해서 for문 하나 더 만드는 것이 훨씬 빠르다. sum, max는 좋은 함수가 아니다!!!
#그런데도 시간이 316ms이다... 더 빠르게 가능할까..?
