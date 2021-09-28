from sys import stdin
input = stdin.readline

# 현재 도시보다 기름 가격이 싼 도시에 도착하기 전까지 거리만큼 기름 충전
def _13305(city : int, road : list, price : list):
    minprice = price[0]
    min_idx = 0
    idx = 1
    ans = 0
    
    while idx != city:
        if minprice > price[idx]:   # 가격이 싼 도시를 찾으면
            ans += sum(road[min_idx:idx]) * minprice   # 거리만큼의 기름 값
            minprice, min_idx = price[idx], idx   # 가격정보 갱신
            idx += 1   # idx 1 증가
        else:
            idx += 1
        
        if idx == city:   # 마지막 도시에서는 기름을 충전할 일이 없기 때문에 그냥 계산
            ans += sum(road[min_idx:idx]) * minprice
            
    return ans


if __name__ == "__main__":
    city = int(input())
    road = list(map(int, input().split()))
    price = list(map(int, input().split()))
    print(_13305(city, road, price))
