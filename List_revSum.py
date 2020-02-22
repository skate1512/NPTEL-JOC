"""
Given an array A of N numbers (integers), you have to write a program which prints the sum of the elements of array A with the corresponding elements of the reverse of array A.
If array A has elements [1,2,3], then reverse of the array A will be [3,2,1] and the resultant array should be [4,4,4].
"""
x=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(0,x):
	b.append(l[i])
b.reverse()
c=[]
n=0
for i in range(0,x):
	n=l[i]+b[i]
	c.append(n)
for i in range(0,x):
	if(i==(x-1)):
 		print(c[i],end="")
	else:
  		print(c[i],end=" ")