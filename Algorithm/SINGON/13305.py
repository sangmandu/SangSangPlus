import sys
input = sys.stdin.readline
N = int(input())
distance = list(map(int, input().split())) #도시와 도시와의 거리를 리스트에 담는다.
city = list(map(int, input().split())) #각 도시당 기름 L당 가격
price = 0
target = city[0]
for i in range(len(distance)):
    if city[i] < target : #i번째 도시에서 기름을 채웠을 때 더 효율적이라면
        target = city[i] #타겟 변경
    price += target*distance[i]
print(price)
