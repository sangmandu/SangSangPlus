from sys import stdin
input = stdin.readline

# 회의의 끝나는 시간이 빠른 순으로 회의를 세주면 된다.
# 회의의 시작시간과 끝나는 시간이 같은 경우 때문에 시작시간을 기준으로도 정렬을 한 번 해주어야 한다.

def _1931(meet : list):
    stp = 0
    ans = 0
    meet.sort(key = lambda x : x[0])
    meet.sort(key = lambda x : x[1])
    for i in meet:
        if i[0] >= stp:
            ans += 1
            stp = i[1]
    
    return ans


if __name__ == "__main__":
    N = int(input())
    meet = [list(map(int, input().split())) for _ in range(N)]
    print(_1931(meet))
