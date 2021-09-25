n, x = map(int, input().split())
a = input().split()
print(' '.join([b for b in a if int(b) < x]))
