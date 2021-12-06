from sys import stdin
input = stdin.readline

# 카드의 숫자가 작은 카드들을 가지고 합치기 과정을 진행
def _15903(m : int, cards : list):
    for _ in range(m):
        cards.sort()
        cards[0], cards[1] = cards[0] + cards[1], cards[0] + cards[1]

    return sum(cards)

if __name__ == "__main__":
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    print(_15903(m, cards))
