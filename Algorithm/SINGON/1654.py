import sys
input = sys.stdin.readline
k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start, end = 1, max(lan) # 이분탐색 처음과 끝위치

while start <= end:
    mid = (start+end)//2
    counts = 0
    for i in lan:
        counts += i//mid
    if counts >= n:
        start = mid+1
    else:
        end = mid-1
print(end)
