from sys import stdin
input = stdin.readline

def _1946(N : int, score : list):
    # ans = 0
    # score.sort(key=lambda x : x[0], reverse=True)
    # for i in range(N):
    #     for j in range(i + 1, N):
    #         if score[i][1] > score[j][1]:
    #             ans += 1
    #             break
    
    # return N - ans
    
    
    # 서류 등수를 높은 순으로 정렬하면 면접 등수만을 고려하면 된다.
    # 면접 등수를 마지노선 등수와 비교하고 갱신하면서 확인한다.
    # 서류 등수를 낮은 순으로 정렬하면 모든 서류 등수에 대해서 면접 등수를 확인해야하므로 소용없다.
    
    score.sort()
    cnt = 0
    max_rank = score[0][1]
    for i in range(1, N):
        if score[i][1] > max_rank:
            cnt += 1
        else:
            max_rank = score[i][1]
    
    return N - cnt


if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        N = int(input())
        rank = [list(map(int, input().split())) for _ in range(N)]
        print(_1946(N, rank))
