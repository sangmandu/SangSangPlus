from sys import stdin
input = stdin.readline

# 높은 순위를 예상한 사람에게 가능한 높은 순위를 차례대로 부여해 준다면, 불만도는 최소가 될 것.

def _2012(N : int, rank : list):
    rank.sort()
    ans = 0
    for A, B in zip(rank, range(1, N + 1)):
        ans += abs(A - B)
    
    return ans

if __name__ == "__main__":
    N = int(input())
    rank = [int(input()) for _ in range(N)]
    print(_2012(N, rank))
