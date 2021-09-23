import sys
input = sys.stdin.readline
'''
search_best_choice함수는 재귀적이라서 10 9 8과 같은 주식 가격에서 비효율적으로 동작하는 것 같다.
차라리 for문아니 while문과 같은 loop를 활용하는 것이 좋아보였다. 또 해당 방식으로는 백준문제에서 메모리 초과 오류가 발생한다.
동작 과정은 아래와 같이 배열의 길이가 0일때까지 반복해주며
배열의 길이가 0이 아닐때는 현재 배열에서 max_price와 해당 Index를 찾고 해당 구간에서의 주식을 사고 판 값을 구해주며(max_price - sum(max index이전값))
return 현재 구간의 값 + search_best_choice(stocke_price_list[max_price_index+1:])를 통해서 이후의 구간의 값들을 구해준다.
'''
def search_best_choice(stock_price_list):
    if len(stock_price_list) <= 0:
        return 0
    max_price = max(stock_price_list)
    max_price_index = stock_price_list.index(max_price)
    current_price = max_price_index * max_price - sum(stock_price_list[:max_price_index])
    return current_price + search_best_choice(stock_price_list[max_price_index+1:])

'''
최댓값 - 현재 index의 stock_price를 계산해서 더해주고 
만약 max_price와 같은 값에 도달했을때는 새로운 max_price값과 찾아준다.
위와 같은 동작을 반복해서 해서 가장 큰 이득을 볼 수 있는 값을 구해주면 된다.

처음에는 위와 같은 방식이 아닌 max_price_index도 찾아줘서 for문 안에 있는 if문을 비교할때
index i가 max_index인지를 비교하는 조건문을 사용하였고 이때 max_price_index와 같을때 새로운 max_price와 max_price_index를 찾아줘야 하는데
find로 index 찾는부분에서 비효율적인 것 같아서 제거해줌
'''
def loop_best_choice(stock_price_list):
    max_price = max(stock_price_list)
    # max_price_index = stock_price_list.index(max_price)
    result = 0
    for i in range(len(stock_price_list)):
        if stock_price_list[i] == max_price:
            stock_price_list[i] = 0
            max_price = max(stock_price_list)
            # max_price_index = stock_price_list.index(max_price)
        else:
            result += max_price - stock_price_list[i]
            stock_price_list[i] = 0

    return result


def solve(test_case):
    for _ in range(test_case):
        days = int(input())
        stock_price_list = list(map(int, input().split()))
        result = loop_best_choice(stock_price_list)
        print(result)
        
if __name__ == '__main__':
    test_case = int(input())
    solve(test_case)



