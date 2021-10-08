from sys import stdin
import heapq
input = stdin.readline

def _11000(cls_time : list):

    '''
    현재 강의의 끝나는 시간과 이전 강의들의 끝나는 시간들을 모두 비교해
    현재 강의의 끝나는 시간이 더 빠르다면 새로운 강의실을 배정해야 하므로
    강의 끝나는 시간을 리스트에 추가
    현재 강의의 끝나는 시간이 더 늦다면 가장 빨리 끝나는 강의실에 배정하므로
    해당 강의실의 끝나는 시간 갱신
    이렇게 생각했는데 답을 보고나니 가장 강의시간이 빨리 끝나는 강의실만 생각하면
    끝나는 것이었습니다...
    가장 빨리 끝나는 강의보다 시작 시간이 빠르다는 것은 나머지 모든 강의들 보다도 빨리 끝나는 것이라서
    그리고 시작시간이 늦다면 강의실을 최소로 배정해야하기 때문에 이전에 풀어봤던
    한 회의실에 최대의 회의를 배치하는 경우처럼 강의실을 배정할 것이기 때문에
    '''

    # 시간 초과(예상은 했지만 혹시나 하는 마음에 돌려본...ㅋㅋ)
    # ans = []
    # cls_time.sort()
    # stp_time = cls_time.pop(0)[1]
    # ans.append(stp_time)
    # for srt, stp in cls_time:
    #     for idx, std in enumerate(ans):
    #         if srt >= std:
    #             ans[idx] = stp
    #             break
    #     else:
    #         ans.append(stp)    
    
    # return len(ans)

    ans = []
    # cls_time.sort(key=lambda x:x[1])
    cls_time.sort()
    heapq.heappush(ans, cls_time.pop(0)[1])

    for srt, stp in cls_time:
        if srt < ans[0]:
            heapq.heappush(ans, stp)
        else:
            heapq.heappop(ans)
            heapq.heappush(ans, stp)
    
    return len(ans)


if __name__ == "__main__":
    N = int(input())
    cls_time = [list(map(int, input().split())) for _ in range(N)]
    print(_11000(cls_time))
