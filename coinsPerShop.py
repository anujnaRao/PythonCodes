n = int(input())
x = int(input())
li = [1,2,3,4,5,6]
sum = cSum = temp = 0
j = 1
sum += li.pop(0) + li.pop()
print(sum)
while j <= len(li):
    for i in range(0,len(li)):
        temp += li[i]
    
    cSum += x*(len(li))
    
    if temp > cSum and len(li) <= 3:
        sum += cSum
        break
    else:
        k = li.pop(j)
        sum += k
    j += 1
  
print(sum)
    
