# 처음 시도한 방식
# import sys
#
# input = sys.stdin.readline
# n = int(input())
# data_list = list(map(int, input().split()))
# dp = [0, data_list[0]]
#
# for i in range(1,n):
#     min_temp = min(data_list[i-1], data_list[i])
#     max_temp = max(data_list[i-1], data_list[i])
#     if min_temp > dp[-2] and dp[-1] > min_temp:
#         if dp[-2] == 0:
#             dp.append(min_temp)
#             dp[-2] = min_temp
#         else:
#             dp[-1] = min_temp
#         continue
#
#     if max_temp > dp[-1]:
#         dp.append(max_temp)
# print(dp)
# print(len(dp)-2)


# 치팅한 방식
import sys

input = sys.stdin.readline

# lower-bound 이진 탐색 방식
def binary_search(start, end, target, data):
    if start == end:
        return end

    mid = (start+ end) // 2

    if data[mid] > target:
        return binary_search(start, mid, target, data)
    elif data[mid] < target:
        return binary_search(mid+1, end, target, data)
    else:
        return mid

def solve():
    n = int(input())
    data_list = list(map(int, input().split()))
    dp_table = [data_list[0]]

    for target in data_list[1:]:
        if target > dp_table[-1]:
            dp_table.append(target)
        else:
            change_index = binary_search(0, len(dp_table)-1, target, dp_table)
            dp_table[change_index] = target

    print(len(dp_table))

if __name__ == '__main__':
    solve()