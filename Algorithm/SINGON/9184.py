import sys
input =sys.stdin.readline
def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)
    
    if dp[a][b][c]:
        return dp[a][b][c]
    if a<b<c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) -w(a,b-1,c)
    else:
        dp[a][b][c] = w(a-1, b,c) + w(a-1,b-1,c) + w(a-1, b, c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]

if __name__ == "__main__":
    dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range (21)] #a>20 or b>20 or c>20일 시 w(a, b, c) == w(20, 20, 20)이 되므로 range(21)까지 해주는 것이다.
    while True:
        a, b, c = map(int, input().split())
        if a==-1 and b==-1 and c==-1:
            break
        print("w({}, {}, {}) = {}".format(a, b, c, w(a,b,c)))
