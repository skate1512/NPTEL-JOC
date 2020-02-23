"""
You are given a number A which contains only digits 0's and 1's. 
Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 ) only. 
If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.
"""
x=input()
count0=0
count1=0
for i in range(len(x)):
  if(x[i]=='0'):
    count0=count0+1
  else:
    count1=count1+1
if(count0==1 or count1==1):
  print("YES",end="")
else:
  print("NO",end="")