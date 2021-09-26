import sys
input = sys.stdin.readline
def recruit(N):
    V = [tuple(map(int,input().split())) for _ in range(N)] #Volunteer의 (서류등수, 면접등수)를 넣음
    V.sort() # 자동으로 x[0], x[1] 작은 순으로 정렬
    cnt = 1 # 처음 타겟 맨 V[0][1]은 입사 가능
    target = V[0][1]
    for i in range(1, N):
        if target > V[i][1]: #V[i] 입사 가능
            cnt +=1
            target = V[i][1] #V[i] 이후의 사람보다는 서류등수 높은거 확정이고 면접등수만 비교하면 되는데 V[i]가 기존 타겟보다 면접등수 높으므로 target을 변경해야한다.
    print(cnt)

if __name__== "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        recruit(N)
