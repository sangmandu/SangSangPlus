'''
그리디 문제라서 모든 경우를 다 해보고 그때 마다 나온 결과값에서 가장 최적의 값을 갖도록
코드를 짠 것 같은데 제출하자마자 틀렸습니다.-라고 뜹니다 ㅠㅠ
아무래도 제 코드에서 이상한 부분이 있는 것 같은데 2시간정도 삽질했는데도 못 찾아서 오늘도 실패... ㅠㅠ
'''
n, l = map(int, input().split())
problem_list = list(map(int, input().split()))
count = 0
filter_list = [] #테이프로 감을 수 있는 범위 내의 있는 것을 담는 list, 이때 해당 지점의 index를 넣어준다.
problem_list.sort()
min_count = 123456789

for i in range(len(problem_list)): # 모든 경우를 다 찾아주기 위해서 사용하는 for문, 예를 들어서 i=2이면 이전 index의 0, 1부분은 각각 1개의 테이프를 사용한 걸로 생각하고
                                    # 2번째 index부터 tape의 길이를 고려하여 포함시킬 수 있는 것을 찾도록 함.
    count = i+1
    filter_list = [] # 매번 테이프에 포함될 수 있는 것을 append하고 해당 index부분은 넣어가기 위해서 사용하는 list
    for start in range(i, len(problem_list)):
        if start in filter_list: # 만약 특정 tape 범위 내에 들어갔다면 해당 부분은 skip해주기 위해서 사용
            continue
        remain = float(l)
        remain -= 0.5 # 양 옆을 0.5씩 추가로 붙여주기 때문에 먼저 맨 왼쪽먼저 붙여주는 의미.
        if start != i:
            count += 1

        for end in range(start+1, len(problem_list)):
            remain = float(remain-(problem_list[end]-problem_list[start])-0.5) #위에서 맨 왼쪽을 붙여주었고 이제는 맨 왼쪽부터 맨 오른쪽까지 테이프 1개로 해결할 수 있는지 체크
            if remain >= 0:
                remain += 0.5 # 만약 더 포함할 수 있다면 이 부분이 맨 오른쪽이 아닐 수 있으므로 0.5를 다시 더해준다.
                filter_list.append(end)
            else: # 음수이면 테이프가 부족하다는 뜻이므로 새 테이프를 사용해야하므로 break를 통해서 빠져나오고 remain = l <- 새로운 테이프 사용한다는 의미.
                break

    min_count = min(min_count, count)


print(min_count)

