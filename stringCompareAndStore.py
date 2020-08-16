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

#Another method of doing just using function

output = []

def checkuser(user):
    if user not in output:
        output.append(user)
        # return user
    else:
        i = 1
        temp =user
        while temp in output:
            temp = user+ str(i)
            i += 1
        output.append(temp)
        # return temp

args= input().split(" ")
out = []
for i in args:
    # out.append(checkuser(i))
    checkuser(i)
# print(out)
print(output)

#Another method of doing using Class

class Uses:
    def __init__(self):
        self.output = []
    
    def checkuser(self, user):
        if user not in self.output:
            self.output.append(user)
            return user
        else:
            i = 1
            temp = user
            while temp in self.output:
                temp = user + str(i)
                i += 1
            self.output.append(temp)
            return temp

if __name__ == "__main__":
    s = input().split(" ")
    ob = Uses()
    s1 = list(map(ob.checkuser, s))
    print(s1)
