import pprint
import sys
input = sys.stdin.readline

'''
저는 2가지 시도를 해보았고 2번째 방식(solve2)만 통과하였습니다.

먼저 실패한 접근 방식인 solve1은 회의시간이 짧은 순서대로 회의 스케쥴표에 넣는 방식을 사용하였습니다.
해당 방식의 문제점은 회의 시간이 짧은 것만 선택하여 부분적으로 본다면 좋은 선택이겠지만 전체적으로 봤을때는 공백인 시간이 많이 발생하게 됩니다.
백준에서의 예제 입력을 가지고 설명을 한다면
최적의 값은 [1,4], [5,7], [8,11], [12,14]이지만
제가 접근한 방식으로 문제를 풀게된다면 회의시간이 짧고 시작시간이 빠른 순서대로 정렬이 되어
[3,5], [5,7], [12,14]를 선택하게 됩니다.
그러므로 solve1번은 올바른 접근법이 아니었습니다.

solve2에서는 단순하게 끝나는 다음 두 조건을 통해서 정렬을 해주었습니다.
1. 종료 시간이 빨라야 한다. 2. 1번의 시간이 동일할 시 시작시간이 빠른 순서로 정렬을 한다.
위의 규칙대로 정렬을 해준뒤 문제를 풀게되면 올바른 결과를 얻을 수 있게 됩니다.


'''
def solve2(test_case):
    meeting_list = [list(map(int, input().split())) for _ in range(test_case)]
    meeting_list.sort(key= lambda x : (x[1], x[0]))
    current = -1
    count = 0
    for target in meeting_list:
        start = target[0]
        end = target[1]
        if current <= start: # 시작시간과 끝나는 시간이 동일한 경우도 있으므로 <=를 사용해줘야 한다.
            count += 1
            current = end
    print(count)





def solve1(test_case):
    meeting_list = [list(map(int, input().split())) for _ in range(test_case)]
    stand_list = [[i, time_arr[1]-time_arr[0]] for i, time_arr in enumerate(meeting_list)] # index와 해당 index의 회의 사간을 구해서 2차원 배열로 만들어줌
    stand_list.sort(key=lambda x : (x[1], x[0]))
    current = -1
    count = 0
    for index, take_time in stand_list:
        start = meeting_list[index][0]
        end = meeting_list[index][1]

        if current <= start:
            count += 1
            current = end

    print(count)




if __name__ == '__main__':
    test_case = int(input())
    solve1(test_case)