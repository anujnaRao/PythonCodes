output = []
print("Enter")
args = input().split(" ")
for user in args:
    if user not in output:
        output.append(user)
        # print("Add to list: ", output)
    else:
        i = 1
        temp = user
        while temp in output:
            temp = user + str(i)
            i += 1
        output.append(temp)

print(output)

# print("enter")
# args = input().split(" ")
# for i in args:
#     li.append(i)
# count = 1
# output = []
# output.append(li[0])
# for i in range(len(li) + 1) :
#     j = i + 1
#     while j < len(li):
#         if li[i] == li[j]:
#             count = count + 1
#             li[j] = li[j] + str(count)
#         else:
#             output.append(li[j])
#             j += 1
#             continue
# print(output)
