#avg of numbers in string
'''
from functools import reduce
n=input("enter the number\n").split()
l=list(map(int,n))
res=reduce(lambda x,y:x+y,l)
avg=res/len(l)
print("{0:.4f}".format(avg))
 
output:enter the number
12 14 18 22 26
18.4000
'''
'''
a=input()
sum=0
for i in range(int(a)):
    b=input()
    sum=sum+int(b)
    avg=sum/int(a)
print(avg)  
'''

'''
n=int(input())
c=0
for i in range(1,n+1):
    c=c+len(str(i))
print(c)
'''


#integer to binary,octa and hexa
'''
a=70
print("{0:b}".format(a))
print("{0:o}".format(a))
print("{0:x}".format(a))
'''
'''
import math
nam="pavan"
place="beng"
print("{} {}".format(nam,place))
print(f"{nam} {place}")
print(f"{math.pi:.4f}")
s="{0:*<10}".format(999)
print(s)
print(f"{math.pi:*^10.4f}")

a=70
print(f"{a:b}")
print(f"{a:o}")
'''

#match fuction:- This function it search the given word only in
#staring means if you give a word that is present in first word in
#the string at that time it matches it not present at first it gives as none
#to overcome this problem we use search
'''
import re
a="python is super easy"
b=r"python"
match=re.match(b,a)
print(match)
start,end=match.span()
print(a[start:end])

output:<re.Match object; span=(0, 6), match='python'>
'''

'''
import re
a="python is super easy"
b="super"
match=re.match(b,a)
print(match)

output:-none
'''

#search function :-it is also a re type,if you use this function it searches the entire string
#and gives the required string



'''
import re
a="python is super easy"
b="super"
match=re.search(b,a)
print(match)
start,end=match.span()
print(a[start:end])

output:<re.Match object; span=(10, 15), match='super'>
super

'''

#In this example we dont use span(),directly use assian the start and end values
'''
import re
a="python is super easy"
b="super"
match=re.search(b,a)
print(match)
print(a[match.start():match.end()])

output:<re.Match object; span=(10, 15), match='super'>
super
'''
'''
a=input()
b=len(a)
for i in range(1,b+1):
    print(a[0]+(a[1:b-3]*i)+a[b-3:b])

output:google
google
goooogle
goooooogle
goooooooogle
goooooooooogle
goooooooooooogle
'''

'''
a="google"
b=len(a)
print(a[b-3:b])
'''

a="google"
b=len(a)
print(a[b::- 2])
#print(a[b-1:b-4:-1])
