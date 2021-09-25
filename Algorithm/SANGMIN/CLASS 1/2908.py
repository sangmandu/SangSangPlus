a, b = input().split()
print(a[::-1] if int(a[::-1]) > int(b[::-1]) else b[::-1])
