from sys import stdin

input = stdin.readline

# 누적 리스트 만든 후 누적합 계산
def _11659(N : int, M : int, arr : list):
    acc_sum = [0] * (N + 1)
    
    for i in range(1, N + 1):
        acc_sum[i] = acc_sum[i - 1] + arr[i - 1]
    
    for _ in range(M):
        srt, stp = map(int, input().split())
        ans = acc_sum[stp] - acc_sum[srt - 1]
        print(ans)
        

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    _11659(N, M, arr)
