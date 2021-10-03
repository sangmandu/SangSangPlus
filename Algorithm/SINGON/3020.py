import sys
input = sys.stdin.readline
N, H = map(int, input().split())

down = [0]*(H+1) # 석순
up = [0]*(H+1) #종유석

min_count = N # 파괴해야하는 장애물의 최솟값
range_count = 0 #최솟값이 나타나는 구간의 수

for i in range(N): #N개의 기둥(?)에서
    if i%2 ==0: #석순
        down[int(input())] += 1 #석순[길이] 추가
    else: #종유석
        up[int(input())] +=1 #종유석[길이] 개수 추가

for i in range(H-1, 0, -1): #이부분에서 누적합이 쓰일줄은 몰랐네요...
    down[i] += down[i+1]
    up[i] += up[i+1]
for i in range(1, H+1):
    if min_count> (down[i] + up[H-i+1]):
        min_count = (down[i]+up[H-i+1])
        range_count =1
    elif min_count == (down[i]+up[H-i+1]):
        range_count +=1
print(min_count, range_count)
    
