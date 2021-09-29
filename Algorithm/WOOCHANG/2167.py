# 시간 초과 ㅠㅠㅠㅠ
import sys

input = sys.stdin.readline


def solve(n,m):
    arr = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    k_list = [list(map(int, input().split())) for _ in range(k)]

    for target in k_list:
        i, j, x, y = target
        result = [arr[i_x][j_y] for i_x in range(i-1,x) for j_y in range(j-1,y)]
        print(sum(result))

if __name__ == '__main__':
    n, m = map(int, input().split())
    solve(n,m)