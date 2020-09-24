def days(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    c = 2
    n = 2
    for _ in range(0, x):
        temp = 0
        temp = n * 2
        c += 1
        n = temp
        print(temp, ":", n)
        if n >= x:
            break
    return c

if __name__ == '__main__':
    x = input()
    d = days(int(x))
    print(d)