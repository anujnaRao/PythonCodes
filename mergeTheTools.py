def merge_the_tools(string, k):
    # your code goes here
    while string:
        s = string[0:k]
        val = ''
        for i in s:
            if i not in val:
                val += i
        print(val)
        string = string[k:]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
