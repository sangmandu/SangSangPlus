import sys

input =sys.stdin.readline
n = int(input())
dp_table = [[-1 for _ in range(i+1)] for i in range(n)] # dp를 위한 table
triangle_list = [list(map(int, input().split())) for _ in range(n)] # input으로 들어오는 값을 담은 list
dp_table[0][0] = triangle_list[0][0]

'''
solve에서 layer와 index를 통해서 최댓값을 구해준다. 이때 dp_table에 값이 -1이면 최댓값으로 초기화가 안 되었다는 의미
이므로 초기화를 시켜준다.
또 해당 layer의 양끝쪽 인덱스는 max를 비교할 필요가 없고 사이의 있는 값들만 max로 비교해주면 된다.
'''
def solve(layer, index):
    if dp_table[layer][index] == -1:
        if index > 0 and index < layer:
            dp_table[layer][index] = max(triangle_list[layer][index] + solve(layer-1, index-1), triangle_list[layer][index] + solve(layer-1, index))
            return dp_table[layer][index]
        elif index == 0:
            dp_table[layer][index] = triangle_list[layer][index] + solve(layer-1,index)
        else:
            dp_table[layer][index] = triangle_list[layer][index] + solve(layer - 1, index-1)

    return dp_table[layer][index]

for i in range(n):
    solve(n-1,i)

print(max(dp_table[n-1]))