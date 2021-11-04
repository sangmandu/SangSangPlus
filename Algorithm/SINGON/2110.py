import sys
input = sys.stdin.readline
n, c = map(int, input().split())
h= [int(input()) for _ in range(n)] #house 좌표
h.sort() #house 좌표 오름차순으로 정렬
start = 1 #최소 거리
end = h[-1] - h[0] #최대 거리
result = 0
while(start<=end):
    mid = (start+end)//2
    value = h[0] #타겟
    count = 1
    for i in range(1, len(h)):
        if h[i] >= value+mid:
            value = h[i]
            count +=1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid-1
print(result)
