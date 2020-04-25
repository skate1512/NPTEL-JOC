"""
Q.Print top 10 most common words in romeo.txt
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
"""
fopen=open("romeo.txt")
counts={}
for line in fopen:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

l=[]
for key,val in counts.items():
    newtup=(val,key)
    l.append(newtup)

l=sorted(l,reverse=True)

for val,key in l[0:10]:
    print(val,key)
