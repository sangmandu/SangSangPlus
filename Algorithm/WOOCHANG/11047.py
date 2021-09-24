import sys
input = sys.stdin.readline

'''
동전 최소 개수 그리디 문제는 큰값에서부터 내리차순으로 동전을 세면 된다.
이때 주어진 k보다 큰 동전 금액은 볼 필요가 없으므로 이진 탐색을 통해서 근접한 동전의 index를 찾아주고 그리디 방식으로 문제를 해결하였다.
'''

'''
binary_search는 이진 탐색이지만 quick sort와 비슷한 방식으로 코딩을 하였습니다.
중간 index(std)를 가지고 이진 탐색을 하고 start_index, end_index가 서로 같거나 엇갈리면 종료하게 됩니다. 또 해당 인덱스 값이 동전과 같은 금액이어도
return 하게 됩니다.
'''
def binary_search(coin_value_list, start_index, end_index,target):
    if start_index >= end_index:
        if abs(coin_value_list[start_index]- target) > abs(coin_value_list[end_index]-target):
            return end_index
        else:
            return start_index

    std = (end_index+start_index) // 2

    if target > coin_value_list[std]:
        return binary_search(coin_value_list, std+1, end_index, target)
    elif target < coin_value_list[std]:
        return binary_search(coin_value_list, start_index, std-1, target)
    else:
        return std

#binary_search를 통해서 얻은 index를 가지고 해당 인덱스부터 0까지 -1씩 증가시키면서 동전을 세줍니다.
def solve(n,k):
    coin_value_list = [int(input()) for _ in range(n)]
    near_index = binary_search(coin_value_list,0,len(coin_value_list)-1,k)
    remainder = k
    count = 0
    for target_index in range(near_index,-1,-1):
        target_coin_value = coin_value_list[target_index]
        if remainder // target_coin_value > 0:
            count += remainder // target_coin_value
            remainder %= target_coin_value

    print(count)

if __name__ == '__main__':
    n, k = map(int, input().split())
    solve(n, k)