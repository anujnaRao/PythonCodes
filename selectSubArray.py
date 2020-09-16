n = 10
# l = [7, 1, 2, 4, 6, 5, 3 ,8 ,9 ,10]
l = [1, 2, 5, 3, 9, 6, 7, 8,10, 0]
l2 = []
l4 = []
i = 1
j = i - 1
mid = (n+j) // 2
while i < mid or j < mid:
    if l[j] > l[i]:
        j += 1
    else:
        l2.append(l[j])
        j += 1
    i += 1 

i = mid +1
j = i - 1    
l3 = []

while i < n and j <= n:
    if l[j] > l[i]:
        j += 1
    else:
        l3.append(l[i])
        j += 1
    i += 1  

if l2[-1] < l[mid -1] and l[mid - 1] < l3[0]:
    l2.append(l[mid-1])
    
l4.extend(l2)
l4.extend(l3)
# print(l4)
print(len(l4))
