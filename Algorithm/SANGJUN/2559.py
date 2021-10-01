from sys import stdin

input = stdin.readline

# 평범한 누적합 문제처럼 누적 배열을 구한 후,
# 날 수 만큼의 합이 담겨있는 배열을 구하고 최대값을 구한다.
def _2559(N : int, K : int, arr : list):
    acc_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        acc_sum[i] = acc_sum[i - 1] + arr[i - 1]
    
    ans = []
    for i in range(K, N + 1):
        ans.append(acc_sum[i] - acc_sum[i - K])
    
    return max(ans)


if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(_2559(N, K, arr))
