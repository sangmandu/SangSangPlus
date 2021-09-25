from sys import stdin
input = stdin.readline

# 구멍 사이의 간격이 테이프 길이 보다 크다면 테이프를 하나 더 사용해야 한다.
# 동시에 테이프를 붙히는 기준점을 갱신해 주어야 한다.

def _1449(N: int, L : int, loc : list):
    ans = 1
    loc.sort()
    srt = loc[0]
    for i in range(1, N):
        if srt + L - 1 < loc[i]:
            ans += 1
            srt = loc[i]

    return ans

if __name__ == "__main__":
    N, L = map(int, input().split())
    loc = list(map(int, input().split()))
    print(_1449(N, L, loc))
