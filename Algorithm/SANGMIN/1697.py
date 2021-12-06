'''
https://www.acmicpc.net/problem/1697
숨바꼭질
[풀이]
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
if K <= N:
    print(N-K)
else:
    size = (2*K)
    board = [K-N+1] * size
    ans = board[N] = 0
    stack, save = [N], []
    while True:
        if not stack:
            stack, save = save, stack
            ans += 1
        n = stack.pop()
        if n == K:
            break
        if n-1 >= 0 and board[n-1] > board[n] + 1:
            board[n-1] = board[n] + 1
            save.append(n-1)
        if n+1 <= size and board[n+1] > board[n] + 1:
            board[n+1] = board[n] + 1
            save.append(n+1)
        if 2 * n <= size and board[2*n] > board[n] + 1:
            board[2*n] = board[n] + 1
            save.append(2*n)
    print(ans)
