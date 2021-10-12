from sys import stdin

input = stdin.readline

# 저번에 풀었던 브1 문제랑 동일
# 2차원 배열의 부분합 그대로 적용
def _11660(N : int, M : int, arr : list):
    acc_sum = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            acc_sum[i][j] = acc_sum[i - 1][j] + acc_sum[i][j - 1] - acc_sum[i - 1][j - 1] + arr[i - 1][j - 1]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        ans = acc_sum[x2][y2] - (acc_sum[x1 - 1][y2] + acc_sum[x2][y1 - 1] - acc_sum[x1 - 1][y1 - 1])
        print(ans)
         

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    _11660(N, M, arr)
