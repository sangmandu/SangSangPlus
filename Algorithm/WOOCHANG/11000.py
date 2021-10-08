'''
강의 시작 시간과 종료 시간을 입력을 받아서 정렬을 해준 후
for문에서 start_time, end_time으로 값을 받고 studing_lecture_list에 end_time을 넣어주고 count를 1증가 시킨다.
이때 studing_lecture_list의 for문을 다 돌았는데 start_time이 모든 studing_lecture_list의 값보다 작으면 새로운 강의실이 필요하고
값이 같거나 크면 해당 강의실을 이어서 사용하면 되니까 count를 증가시키지 않고 해당 studing_lecture_list[index]의 값을
end_time으로 바꿔주는 알고리즘이다.
'''
import sys

input = sys.stdin.readline

def solve(n):
    schedule_list = [list(map(int, input().split())) for _ in range(n)]
    schedule_list.sort()
    studing_lecture_list = []
    count = 0

    for start_time, end_time in schedule_list:
        if len(studing_lecture_list) == 0:
            studing_lecture_list.append(end_time)
            count += 1
            continue

        for index in range(len(studing_lecture_list)):
            if start_time >= studing_lecture_list[index]:
                studing_lecture_list[index] = end_time
                break

            if len(studing_lecture_list)-1 == index:
                count +=1
                studing_lecture_list.append(end_time)


    print(count)


if __name__ == '__main__':
    n = int(input())
    solve(n)