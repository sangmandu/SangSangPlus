"""숫자가 규칙이 존재
1*1~ 1*n
2*1~ 2*n
. . .
n*1~n*n
B[k] = answer 이라 할 때
answer 이하의 개수는
min(answer//1,n)+min(answer//2,n)+...min(answer//n, n)이다."""
n = int(input())
k = int(input())
start, end = 1, k
while start <=end:
    mid = (start+end)//2
    temp = 0
    for i in range(1, n+1):
        temp += min(mid//i, n)
    if temp>=k:
        answer = mid
        end = mid-1
    else:
        start = mid+1
print(answer)