'''
1. 최고점까지는 무지성 매수 후 최고점에서 모두 파는 행동을 반복
2. 최고점에서 팔면 리스트를 다음날 부터의 정보만을 가지고 있도록 갱신
3. 다시 최고점을 찾아 위의 행동을 반복한다.

시간초과에 걸리지 않기 위해 남은 가격의 변동이 없는 경우 바로 반복문을 종료.
첫 날 부터 가격이 계속 내려가기만 하는 경우에도 반복문을 종료. 
시간이 단축될 것 같은데 코드로 구현을 하지 못함. -> 이것때문에 채점하는데만 2분이 걸린거 같음.
'''

from sys import stdin
input = stdin.readline

def _11501(days : int, prices : list):
    
    ans = 0

    while prices:
        buy_price = 0
        max_idx = prices.index(max(prices))  # 최고점 idx
        buy_price += sum(prices[:max_idx])  # 최고점까지 풀 매수
        ans += prices[max_idx] * max_idx - buy_price  # 최고점에서 모두 익절
        prices = prices[max_idx + 1:]  # 가격정보 갱신

        # decrease_price = sorted(prices, reverse=True)

        # if decrease_price == prices:
        #     break
        # -> 매번 정렬이 시간 더 잡아먹어서 시간초과

        if len(set(prices)) == 1:  # 가격정보에 변동이 없다면 반복문 종료
            break

        

    return ans


if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        days = int(input())
        prices = list(map(int, input().split()))
        print(_11501(days, prices))
