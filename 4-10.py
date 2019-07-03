q=int(input())
f1,f2=0,1
print(f2,end=" ")
for i in range(1,q):
 f3=f1+f2
 print(f3,end=" ")
 f1,f2=f2,f3
