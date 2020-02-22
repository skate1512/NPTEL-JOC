"""
Given a list of numbers (integers), find second maximum and second minimum in this list.
"""
l=list(map(int,input().split()))
l.sort()
print(l[len(l)-2],l[1],end="")