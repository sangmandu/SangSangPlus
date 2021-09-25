a = int(input())
cond = a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)
print(1 if cond else 0)
