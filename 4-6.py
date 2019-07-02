x=input()
p=0
for i in range(len(x)):
 if(x[i].isdigit() or x[i].isalpha() or x[i]==(" ")):
  continue
 else:
  p+=1
print(p)
