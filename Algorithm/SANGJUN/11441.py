from sys import stdin
input = stdin.readline

# 누적합을 기록할 배열 생성 후 배열의 원소 차로 구간합 구하기.
def _11441(N : int, M : int, arr : list):
    acc_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        acc_sum[i] = acc_sum[i - 1] + arr[i - 1]

    for _ in range(M):
        srt, stp = map(int, input().split())
        ans = acc_sum[stp] - acc_sum[srt - 1]
        print(ans)


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    _11441(N, M, arr)
