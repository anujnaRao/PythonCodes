if __name__ == '__main__':
    N = int(input())

    lis = []
    for t in range(N):
        args = input().split(" ")
        if args[0] == "append":
            lis.append(int(args[1]))
        elif args[0] == "insert":
            lis.insert(int(args[1]), int(args[2]))
        elif args[0] == "remove":
            lis.remove(int(args[1]))
        elif args[0] == "pop":
            lis.pop()
        elif args[0] == "sort":
            lis.sort()
        elif args[0] == "reverse":
            lis.reverse()
        elif args[0] == "print":
            print(lis)
