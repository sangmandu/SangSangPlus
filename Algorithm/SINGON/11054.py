import sys
input = sys.stdin.readline
def solution(N,A):
    if N==1 or N==2: #Trivial
        return N
    dp = [0]*1001
    dn = [0]*1001
    for i in range(1,N+1):
        maximum = 0
        for j in range(i):
            if A[j] < A[i]:
                if dp[j] >= maximum:
                    maximum = dp[j]
        dp[i] = maximum+1 #i 번째 까지의 증가수열의 최대 길이
    for i in range(N,0,-1):
        reverse_maximum = 0
        for j in range(N,i-1,-1):
            if A[j] < A[i]:
                if dn[j] >= reverse_maximum:
                    reverse_maximum = dn[j]
        dn[i] = reverse_maximum+1 #i 번째부터 N까지의 감소함수의 최대 길이
    ds = [0]*1001
    for i in range(0,N+1):
        ds[i] = dp[i]+dn[i]
    return(max(ds)-1) #i번째 길이를 셀 때 두 번 더했으므로 -1이 필수!
if __name__ == "__main__":
    N = int(input())
    A = [0] + list(map(int,input().split()))
    print(solution(N,A))
