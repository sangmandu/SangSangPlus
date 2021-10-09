import sys
input = sys.stdin.readline
N = int(input())
All = []
All.append([0, 0, 0])
for _ in range(N):
    All.append(list(map(int, input().split()))) # i번째 (R, G , B) 가격 All에 입력
for i in range(1,N+1):
    All[i][0] = min(All[i-1][1], All[i-1][2]) + All[i][0]
    All[i][1] = min(All[i-1][0], All[i-1][2]) + All[i][1]
    All[i][2] = min(All[i-1][0], All[i-1][1]) + All[i][2]
print(min(All[N][0], All[N][1], All[N][2]))

