from sys import stdin
input = stdin.readline

def _2167(subtotal : list, dp : list):
    i, j, x, y = subtotal
    
    # ans = 0
    # for row in range(i, x + 1):
    #     ans += sum(matrix[row][j : y + 1])
    
    # return ans

    return dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1]


if __name__ == "__main__":
    N, M = map(int, input().split())
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = matrix[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
    K = int(input())
    for _ in range(K):
        subtotal = list(map(int, input().split()))
        print(_2167(subtotal, dp))
