if __name__ == '__main__':
    s = input()
    
    a, b, c, d, e = False, False, False, False, False

    str = list(s)

    for i in str:
        if i.isalnum():
            a = True
        if i.isalpha():
            b = True
        if i.isdigit():
            c = True
        if i.islower():
            d = True
        if i.isupper():
            e = True
    print(a)
    print(b)
    print(c) 
    print(d)
    print(e)

    # Second method
    # for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    #     print(any(method(c) for c in s))
