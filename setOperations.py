def average(array):
    val = set(array)
    avg = sum(val) / len(val)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
