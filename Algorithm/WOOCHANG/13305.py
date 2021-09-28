import sys

input = sys.stdin.readline

def element_mal(x,y): # 밑에서 거리와 가격을 곱하는 연산 수행할때 사용할 함수
    return x * y

def solve(n):
    distance_list = list(map(int, input().split())) # 거리 정보
    oil_price_list = list(map(int, input().split())) # 기름 가격
    strategy_list = [0 for _ in range(len(distance_list))] # 다음 도시까지 가장싼 가격으로 가기 위한 기름 가격
    strategy_list[0] = oil_price_list[0] # 처음에는 무조건 기름을 넣어야 한다
    cheap_oil_price = strategy_list[0]

    for index in range(1,len(distance_list)): # 2번째 도시부터 기름 가격을 비교하고 싼 가격을 list에 넣어준다.
        if cheap_oil_price > oil_price_list[index]: #만약 더 싼 가격이 나오면 해당 가격을 cheap_oil_price로 지정하고 넣어준다.
            cheap_oil_price = oil_price_list[index]
        strategy_list[index] = cheap_oil_price

    result_list = map(element_mal, distance_list, strategy_list) #기름가격과 거리간의 원소 곱
    print(sum(result_list)) # 총 합


if __name__ == '__main__':
    num_of_city = int(input())
    solve(num_of_city)