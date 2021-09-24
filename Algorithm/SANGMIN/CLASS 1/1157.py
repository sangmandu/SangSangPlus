string = input().lower()
if len(string) == 1:
    print(string.upper())
else:
    dic = {s : 0 for s in set(string)}
    for s in string:
        dic[s] += 1
    sorted_dic = sorted(dic.items(), key=lambda x : -x[1])
    k, v = sorted_dic[0]
    print('?' if v == sorted_dic[1][1] else k.upper())
