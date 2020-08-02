if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sortedList = sorted(arr)
    
    maxVal = max(sortedList)

    for i in range(0, len(sortedList)):
        if sortedList[i] == maxVal:
            print(sortedList[i-1])
            break
