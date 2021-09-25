n = int(input())
for _ in range(n):
    m, words = input().split()
    print(''.join([word * int(m) for word in words]))
