import sys
import pprint

input = sys.stdin.readline
n = int(input())
dp_table = [[0 for _ in range(n+1)] for _ in range(6)]
data_list = [0] + [int(input()) for _ in range(n)]

for i in range(1,n+1):
    if n <= 2 and n == i:
        print(sum(data_list))
        break

    if i % 3 == 1:
        dp_table[0][i] = data_list[i]
        dp_table[2][i] = data_list[i]
    elif i % 3 == 2:
        dp_table[0][i] = data_list[i]
        dp_table[1][i] = data_list[i]
    else:
        dp_table[1][i] = data_list[i]
        dp_table[2][i] = data_list[i]

    if i == n:
        print(max(sum(dp_table[0]),sum(dp_table[1]), sum(dp_table[2])))

pprint.pprint(dp_table)