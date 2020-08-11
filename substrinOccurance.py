def minion_game(string):
    vowel =['A','E','I','O','U']
    countS=0
    countK=0
    for i in range(len(string)):
        if string[i] in vowel:
            countK += len(string)-i
        else:
            countS += len(string)-i
    if countS > countK:
        print("Stuart {}".format(countS))
    elif countK > countS:
        print("Kevin"+" "+'%d' % countK)
    else:
        print("Draw")


    # kevin = []
    # stuart = []
    # countK = 0
    # countS = 0
    # i = string[0]
    # n = 0
    # while n < len(string):
    #     kev = ''
    #     stu = ''
    #     if i == 'A' or 'E' or 'I' or 'O' or 'U':
    #         kev = kev + i
    #     else:
    #         stu = stu + i
        
    #     for j in range(1,len(string)):
    #         if kev is not '':
    #             for k in range(len(string)):      
    #                 if string[k:].startswith(kev):
    #                     countK += 1
    #             kev += string[j]
                
    #             kevin.append(kev)
        
    #     for j in range(1,len(string)):
    #         if stu is not '':
    #             for k in range(len(string)):      
    #                 if string[k:].startswith(stu):
    #                     countS += 1
    #             stu += string[j]
                
    #             stuart.append(stu)

    #     n += 1

    # if countS > countK:
    #     print("Stuart {}".format(countS))
    # else:
    #     print("Kevin {}".format(countK))


if __name__ == '__main__':
    s = input()
    minion_game(s)
