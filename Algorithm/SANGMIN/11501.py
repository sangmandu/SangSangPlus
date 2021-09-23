'''
https://www.acmicpc.net/problem/11501
주식
[풀이]
1. 핵심은, 두 가지이다.
=> 미래에 가격이 오르면 무조건 현재 산다.
=> 미래에 가격이 최대인 날에 주식을 판다.
2. 또한, 주어진 주식 데이터 길이가 1,000,000 이므로 N^2은 불가능
=> N 으로 진행해야 겠다는 생각을 할 수 있음
3. 이 때, 현재를 기준으로 미래의 데이터를 조사(미래에 가격이 최대인 날을 찾는 과정)하려고 하면 N^2이 소요된다.
=> 따라서, 현재를 기준으로 과거 데이터를 조사하는 방향으로 하자.
4. 그렇게 되면 다음과 같은 통찰을 얻는다.
=> 지금 있는 시점이 가격이 최대라면 과거 시점들은 모두 이 시점에 판매하겠군.
=> 지금 있는 시점이 가격이 최대가 아니라면 지금 시점 보다 값이 비싼 과거 시점에 판매를 하겠군
=> 그리고 그 시점 이후에는 내 시점에서 판매하겠군. (만약 아니라면 또 반복)
5. 이에 대한 구현을 한다.
=> 매번 최대 가격을 구하며, 각각의 시점에서의 가격은 최대 가격에서 팔것이므로 뺀 값을 매번 추가
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    answer = selling_price = 0
    for price in prices[::-1]:
        selling_price = max(selling_price, price)
        answer += selling_price-price
    print(answer)


