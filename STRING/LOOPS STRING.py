#program to iterate any iterable
'''
s= 'python'
#print(' '.join(s))
for i in s:
    print(i,end='')

'''
#print characters in a string
'''
a='qwe1234ert@'
for i in a:
    if(ord(i)>=97 and ord(i)<=122):
        print(i)
#0r
a='qwe1234ert@'
for i in a:
    if(i.isalpha()):
        print(i)
'''
#most repeating word in string
'''
a=input().split()
d={}
for i in a:
    if(i in d):
        d[i]+=1
    else:
        d[i]=1
print(max(d,key=d.get))
print(len(max(d,key=d.get)))
'''

        
#print upper char count in a string
'''
a='asUR123'
c=0
for i in a:
    if(ord(i)>=65 and ord(i)<=90):
        print(i)
        c+=1
print(c)
a='asUR123'
c=0
for i in a:
    if(i.isalpha() and i.isupper()):
        print(i)
        c+=1
print(c)
'''
#l=['pavan','kumar','python']
#output:   ['nohtyp','ramuk','navap']
'''
l=['pavan','kumar','python']
r=[]
for i in l:
    rev=i[0:len(i)][::-1]
    r.append(rev)
print(r[::-1])
'''
#print the words when starts with h
'''
s=input().split()
for i in s:
    if(i.startswith('h')):
        print(i)

#or
s=input().split()
for i in s:
    if(i[0]=='h'):
        print(i)
'''
#most repeating char in string
'''
a=input()
d={}
for i in a:
    if(i in d):
        d[i]+=1
    else:
        d[i]=1
#print(max(d,key=d.get))
m=max(d.values())
for char,count in d.items():
    if(count==m):
        print(char,count)
'''
#first occurance index values
'''
s='aggreate'
a=enumerate(s)
d={}
for i,char in a:
    if(char not in d):
        d[char]=i
print(d)#{'a': 0, 'g': 1, 'r': 3, 'e': 4, 't': 6}
for i,char in d.items():
    print("first occurane is",i,'index:',char)

output:
first occurane is 0 index: a
first occurane is 1 index: g
first occurane is 3 index: r
first occurane is 4 index: e
first occurane is 6 index: t
'''

   
        
#to count no.of each char
'''
s='pavan'
d={}
for i in s:
    if(i in d):
        d[i]+=1
    else:
        d[i]=1
a={}
for j,count in d.items():
    if(j not in  a):
        a[j]=count
print(a)       
output:{'p': 1, 'a': 2, 'v': 1, 'n': 1}
'''
#dict word and its count
'''
s='hello world welcome hello'.split()
d={}
for i in s:
    if(i in d):
        d[i]+=1
    else:
        d[i]=1
print(d)
output;{'hello': 2, 'world': 1, 'welcome': 1}
'''
#print asci values of char in a string
'''
s='pavan'
d={}
for i in s:
    d[i]=ord(i)
print(d)
output:{'p': 112, 'a': 97, 'v': 118, 'n': 110}
'''
#to print vowels in string
'''
s='python selinium'
a=set(a)
for i in s:
    if(i in 'AEIOUaeiou'):
        a+=i
    print(a)
'''
'''
s=input().split('.')
print(''.join(s[1:]))

'''
'''
s="exam's"
l=[True,4,5.6,]
from itertools import zip_longest
for n in zip_longest(s,l):
    print(n,end="")  #('e', True)('x', 4)('a', 5.6)('m', None)("'", None)('s', None)
for n in zip_longest(s,l,fillvalue='a'):
    print(n,end="")  #('e', True)('x', 4)('a', 5.6)('m', 'a')("'", 'a')('s', 'a')
'''
'''
#l=[1,2,3,4]
#s=[1,2,3,4]
l=list(input())
s=list(input())
from itertools import zip_longest
for i,j in zip_longest(l,s):
    print(f'{int(i)}+{int(j)}={int(i)+int(j)}')
'''
#program to square the number in t

'''
s=input().split()
l=input().split()
from itertools import zip_longest
for i,j in zip_longest(l,s):
    #print(((int(i)**2),(int(j)**3)))
     print((f'({int(i)**2},{int(j)**3})'))
'''

#to print number sum in a string
'''
#s='sony12india567'
s=input()
a=0
for i in s:
    if(i.isnumeric()):
        a+=int(i)
print(a)
'''
#to print exacept digits in the string
'''
s=input()
for i in s:
    if(i.isnumeric()):
        continue
    else:
        print(i,end=" ")
output:@hello12world34welcome123
@ h e l l o w o r l d w e l c o m e
'''
#adding first 3 and last 3 char
'''
n=int(input())
a=[]
for i in range(n):
    b=input()
    a.append(b)
print(a[:3]+a[len(a)-3:])
output:['Anjali', 'Ravi', 'Akbar', 'Latha', 'Mohan', 'Ashok']
'''
#duplicate char in a string
'''
s=input()
d=[]
a=set()
for i in s:
    if(i not in d):
        d.append(i)
    else:
        a.add(i)
print(' '.join(a))

output;
asdddaaa
a d
'''

'''
n=input().upper()
a=n.split()
l=[]
for i in a:
    l.append(i[0])
print('.'.join(l))

output:PAVAN KUMAR
P.K
'''

#Write a program to create a new string made of the middle three characters of an input string.
'''
s=input()
a=len(s)
b=int(a/2)
print(b)
print(s[b-1:b+2])
output:
pavankumar1
5
nku

jasonay
3
son
'''
#Append new string in the middle of a given string
'''
s='ault'
s1='kelly'
a=int(len(s)/2)
print(a)
print(s[:a]+s1+s[a:])

output:
aukellylt
'''
#Create a new string made of the first, middle, and last characters of each input string
'''
s1 = "America"
s2 = "Japan"
a=s1[::3]
b=s2[::2]
s=''
c=''
for i in range(len(a)):
    s=s+a[i]
    c=c+b[i]
print(s+c)
output:
AraJpn
'''
#Arrange string characters such that lowercase letters should come first
'''
s = 'PyNaTive'
a=''
b=''
for i in s:
    if(i.islower()):
        a+=i
    else:
        b+=i
print(a+b)

output:
yaivePNT
'''      
#Count all letters, digits, and special symbols from a given string
'''
s="P@#yn26at^&i5ve"
c=0
d=0
e=0
for i in s:
    if(i.isalpha()):
        c+=1
    elif(i.isdigit()):
        d+=1
    else:
        e+=1
print(f'chars = {c}')
print(f'Digits = {d}')
print(f'Symbols = {e}')

output:
chars = 8
Digits = 3
Symbols = 4
'''
 #String characters balance Test
'''
s1 = "Yn"
s2 = "PYnative"
if(s1 in s2):
    print("True")
else:
    print("false")
'''
#Calculate the sum and average of the digits present in a string
'''
str1 = "PYnative29@#8496"
s=0
c=0
for i in str1:
    if(i.isdigit()):
        s+=int(i)
        c+=1
        a=s/c
print(f'sum is:{s} average is {a}')

output: sum is:38 average is 6.333333333333333
'''
#Write a program to find the last position of a substring “Emma” in a given string.
'''
s="Emma is a data scientist who knows Python. Emma works at google."
a=s.index('E',1)
print(f'Last occurrence of Emma starts at index {a}')

output:Last occurrence of Emma starts at index 43
'''
#Remove empty strings from a list of strings
'''
s=["Emma", "Jon", "", "Kelly", None, "Eric", ""]
for i in s:
    if(i==''):
        s.remove(i)
print(s)
'''
#Replace each special symbol with # in the following strin
'''
s="/*Jon is @developer & musician!!"
a=''
for i in s:
    if(i.isalpha() or i==' '):
        a+=i
    else:
        a+='#'
print(a)

output:##Jon is #developer # musician##
'''
