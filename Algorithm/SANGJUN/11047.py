from sys import stdin
input = stdin.readline

# target 값 보다 크지 않은 동전 중 가장 큰 동전으로 바꿀 수 있는 만큼 최대한 바꾼다.
def _11047(K : int, coin : list):
    ans = 0
    trg = K
    for i in coin:
        if i <= trg:
            ans += trg // i
            trg = trg % i
            if not trg:
                break
            
    return ans


if __name__ == "__main__":
    N, K = map(int, input().split())
    coin = [int(input()) for _ in range(N)]
    print(_11047(K, reversed(coin)))
