while True:
    a = input()
    if a == '0':
        break
    print("yes" if a[:len(a)//2+len(a)%2] == a[len(a)//2:][::-1] else "no")
