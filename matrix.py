x,y=map(int,input().split())
count=1
R=[]
for i in range(x):
  C=[]
  for j in range(y):
    C.append(count)
    count=count+1
  R.append(C)  
for i in range(x):
  for j in range(y):
    if(j!=y-1):
      print(R[i][j],end=" ")
    else:
      print(R[i][j],end="")
  if(i!=x-1):
    print()