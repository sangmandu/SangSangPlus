# accumulate를 이용해서 누적한 방식으로 해결하였습니다.

import sys
from itertools import accumulate

input = sys.stdin.readline

def solve(n):
    data_list = list(map(int,input().split()))
    cum_list = list(accumulate(data_list))
    num_section = int(input())
    section_list = [list(map(int, input().split())) for _ in range(num_section)]

    for i, j in section_list:
        new_i, new_j = i-1, j-1
        print(cum_list[new_j]-cum_list[new_i]+data_list[new_i])


if __name__ == '__main__':
    n = int(input())
    solve(n)