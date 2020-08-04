def mutate_string(string, position, character):
    stringList = list(string)
    stringList[position] = character
    string = "".join(stringList)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
