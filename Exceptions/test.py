a = [1, 2 , 3, 4, 5]
a2 = []
t = int(input("Enter "))
for k in range (0,t):
    n = int(input("Enter "))
    for m in range(0,n):
        a.append()
    
    for m in range(0,n):
        print(a)

i = 1
j = 5 -1
while i<5:
    a2.append(a[j] - a[i] - 1)
            
for m in range(0,n):
    print(a)
        
val = max(a2)
print(val)
print(val * val)


# #include <iostream>
# #include <cmath>
# #define MAX 10000
# using namespace std;

# int main(){

#     int a[MAx], a2[MAX],n,t,val;
#     cin >> t;
#     for(int k=0;k<t;k++){
#         cin >> n;
#         for(int m = 0; m <n;m++){
#             cin >> a[m];
#         }

#         for(int m = 0; m <n;m++){
#             cout << a[m];
#         }

#         int i = 1, j = n -1;
#         while( i < n ){
#             a2[i-1] = a[j] - a[i];
#         }
#         for(int m = 0; m <n;m++){
#             cout << a2[m];
#         }
        
#         val = max(a2);
#         cout << val;
#         cout << (val * val);

#     }
# }
