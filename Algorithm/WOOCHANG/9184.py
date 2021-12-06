# 범위가 -50~50까지 이므로 0~101까지의 배열을 만들어 줘서 사용했습니다.
import sys

input = sys.stdin.readline

def solve():
    # a,b,c중에 0이하인 값이 있으면 1 아니면 0을 집어넣어준다.
    dp = [[[0 if a > 50 and b > 50 and c > 50 else 1 for c in range(101)] for b in range(101)] for a in range(101)]

    # 1(51)부터 50(100)까지의 범위를 규칙대로 값을 넣어주었습니다.
    for a in range(51,101):
        for b in range(51,101):
            for c in range(51, 101):
                if a > 70 or b > 70 or c > 70:
                    dp[a][b][c] = dp[70][70][70]
                elif a < b and b < c:
                    dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
                else:
                    dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]



    while True:
        a, b, c = map(int, input().split())
        if a == b == c == -1:
            break

        index_a = a+50
        index_b = b+50
        index_c = c+50
        print(f'w({a}, {b}, {c}) = {dp[index_a][index_b][index_c]}')


if __name__ == "__main__":
    solve()