"""
Given an integer number n, you have to print the factorial of this number.
"""
x=int(input())
f=1
for i in range(1,x+1):
	f=f*i
print(f,end="")