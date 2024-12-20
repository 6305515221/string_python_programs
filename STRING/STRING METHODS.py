  '''
a=input("enter the string:\n")
b=input("enter the string2:\n")
c=a*3
d=b*3
print(a+b)
print(c)
print(d)
print(c+d)


a=int("enter the name:\n")
b=int(input("enter the value:\n"))
print(a+b)

'''


'''
l=str([23,45,12,895,34,23])
print(l)  #[23, 45, 12, 895, 34, 23]


l=['23',24,3+0j,False]
print(l)  #['23', 24, (3+0j), False]

#convert string to list
l="pavan"
print(list(l))  #['p', 'a', 'v', 'a', 'n']

#tuple to list
print(list(("banglore",34,4.5)))
#['banglore', 34, 4.5]


print(list({'banglore':45,34:45,4.5:True}))  #['banglore', 34, 4.5] In dict it gives by default key values

'''

'''
l=[23,45,12,895,34,23]
print(l[3])
print(l[1:4])
'''



'''
l=['23',[45,12,'895'],34.5,23,3+6j,False]
print(l)
print(l[1][2][2],l[-5])
print(l[0][1])


'''

'''
#program to get even index element
l=['23',[45,12,'895'],34.5,23,3+6j,False]
print(l)
print(l[::2])#program to get even index element
print(l[1::2])#program to get odd index element
print(l[::-1])#program to reverse the list
print(l[-2::-2])#program to get even index element in reverse order
print(l[-1::-2])#program to get odd index element in reverse order

'''

'''
l=['23',[45,12,'895'],34.5,23,3+6j,False]
#[45,12,'895'] in reverse
print(l[1][::-1])  #['895', 12, 45]
#'23' reverse
print(l[0][::-1])  #32
print(l[2:5])
print(l[4:2:-1])
print(l[:4:3])
'''

'''
l=['23',[45,12,'895'],34.5,23,3+6j,False]

print(1[:3:2]+l[3])

'''


'''
l=[45,3.5,2.3,"hey",[True,False]]
l[3]="HEy"
print(l)
#[45, 3.5, 'HEy', 'hey', [True, False]]

l[:2]=[3,7]
print(l)
l[2:]="apple"
print(l)
l[2:]=['apple']
print(l)
'''

#Append
'''
l=[2,34.5,'pavan',{1,2,3,4},[True,False]]
l.append(3+0j)
print(l)   #[2, 34.5, 'pavan', {1, 2, 3, 4}, [True, False], (3+0j)]
'''


#extend   it unpack the elements

l=[2,34.5,'pavan',{1,2,3,4},[True,False]]
l.extend('hai')
l.extend(['hai',45,False,7.8])
print(l)      #[2, 34.5, 'pavan', {1, 2, 3, 4}, [True, False], 'h', 'a', 'i', 'hai', 45, False, 7.8]




#insert   we can add any valu like integer and flaot in anu place
'''
l=[2,34.5,'pavan',{1,2,3,4},[True,False]]

l.insert(0,"kumar")  #['kumar', 2, 34.5, 'pavan', {1, 2, 3, 4}, [True, False]]
l.insert(4,45)  #['kumar', 2, 34.5, 'pavan', 45, {1, 2, 3, 4}, [True, False]]
print(l)     


'''

#pop
'''
l=[1,2,3,4,5,67]
l.pop(2)
print(l)


'''


#remove
'''
l=[1,2,3,4,5,6,7,3]
l.remove(3)
print(l)


'''


#del
'''
l=[1,2,3,4,5,6]
del l[2]    #[1, 2, 4, 5, 6]
del l[0:2]    #[3, 4, 5, 6]

print(l)

'''



#reverse
'''
l=[1,2,"45",[1,2,3],True,False]
l.reverse()
print(l)
'''



#index
'''
l=[1,2,0,"45",[1,2,3],True,False]
print(l.index(2))   #1
print(l.index(False))  #2
print(l.index(False,3))  #6

#count
l=[1,2,0,"45",[1,2,3],True,False]
print(l.count(1))#2
print(l.count([2,31,]))  #0
'''



'''
s1,s2="hi guys","how are you"
print(s1,s2 ,sep="\n")




#constructor: str()
#1.
print(type(s3))
#default value: ' ' or " "
print(str())
#typecasting

i,f,c,b=str(1),str(2.2),str(3+4j),str(True)
print(type(i),i)
print(type(i),f)
print(type(i),c)
print(type(i),b)
'''
'''
s=input("enter the string:")
print("string : ",s,"It is the length is:",len(s))
'''



'''
s="bangolre"
print(s,len(s))

print(s[1],s[4])

print(s[1],s[len(s)-1])
print(id(s[1]),id(s[4]))
'''



'''
a=input()
b=len(a)//2
print(a[b])
'''
'''
a=input()
b=len(a)-2
print(a[b])
'''

'''
s=input()
print(s[:3])
'''

'''
print(float("2.5"))
print(int(2+0j))
'''

'''
s="welcome to my channel"
print(s)
print(s[::])
print(s[1::2]) #odd values
print(s[::2])#even values
print(s[:7:2])#in welcome we take even values
print(s[1:7:2])# in welcome we take odd values

output:welcome to my channel
welcome to my channel
ecm om hne
wloet ycanl
wloe
ecm
'''


#s="welcome to my channel"
'''
print(s[::-1])
print(s[len(s)-1:12:-1])
print(s[-1:-8:-1])


print(s[:10])
print(s[10::-1])
print(s[-12::-1])
print(s.index("t"))
print(s[12:7:-1])

'''
#for i in range(len(s)):
    
'''   
#print(s[-9:-14:-1])
s="slicing is tricky"
print(s)
print(len(s))
print(s[::-1])
print(s[6::-1])
print(s[-11::-1])
print(s[9:7:-1])
print(s[-8:-10:-1])
print(s[len(s)-1:10:-1])
print(s[-1:-7:-1])
print(s[12:3:-1])
print(s[-5:-14:-1])
'''
'''
s="welcomec"
a=len(s)
for i in range(a):
    if(s[i]=="c"):
        print(i)
'''
'''
a=0
b=1
for i in range(10):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
        
'''

'''
s="welcome to my channel"
print(s[len(s)-2::-2])#skip even index means odd index
print(s[len(s)::-2])#skip odd index means even char

output:-enh mo mce
lnacy teolw
'''
s="welcome to my channel"
'''
print(s[6::-1])#emoclew
print(s[6::-2])#eolw
print(s[5::-2])#mce
'''
'''
#to my
print(s[12:7:-1])#ym ot
print(s[12:7:-2])#y t
print(s[11:7:-2])#mo

#to my negative index
print(s[-8:-14:-2])
'''


'''
#replace


a="Hello world"
print(a.replace("l","L"))
print(a.replace("Hello","Hai"))#Hai world
print(a.replace("l","L",1))
print(a.replace(a[3],"L"))
print(a.replace("o","@",1))#Hell@ world
print(a.replace("o","@",2))#Hell@ w@rld
a="Hello world"
print(a.replace(a[4],"L"))
'''

'''
#lower()
a=input("enter the string: \n")
print(a.lower())
OUTPUT:enter the string: 
pAVA@23
pava@23
'''
'''
a="pavan kumar"
b=a.replace(a[6:],"KUMAR")
print(b)
'''
'''
a=input("enter the string:\n")
print(a.islower())

a=input("enter the string:\n")
print(a.isupper())

a=input("enter the string:\n")
print(a.isalpha())

a=input("enter the string:\n")
print(a.isalpha())
'''
a=input("enter the string:\n")
print(a.isalnum())

output:enter the string:
qwe12@
False





'''
print(89)
print(5.6,sep="@")
print(3,4,end="*"
)
'''

#startswith()   its only acess index it cannot acess slicing
'''
str1=input("enter")
sub_s=input("substring")
starts=int(input("enter the value"))
print(str1.startswith(sub_s,starts))

output:enterpavan
substringa
enter the value3
True
'''


#endswith()  its only acess index it cannot acess slicing
'''
str1=input("enter:\n")
sub_s=input("substring:\n")
ends=int(input("enter the value:\n"))
#print(str1.endswith(sub_s,0,ends))
print(str1.endswith(sub_s,-1,ends))


output:enter:           
pavan
substring:
a
enter the value:
4
True

enter:
pavan
substring:
a
enter the value:
-2
False

enter:
pavan
substring:
a
enter the value:
-3
True
'''
'''
s="pavan"
print(s.endswith())
'''


'''
s="pavan and jagadeesh are good friends"
print(s.split())  #['pavan', 'and', 'jagadeesh', 'are', 'good', 'friends']
print(s.split("and"))  #['pavan ', ' jagadeesh are good friends']
print(s.split("are"))  #['pavan and jagadeesh ', ' good friends']
print(s.split("a",1))  #['p', 'van and jagadeesh are good friends']
s="pavan-jagadeesh-good friends"
print(s.split("-",1))#['pavan', 'jagadeesh-good friends']
#rsplit
s="pavan and jagadeesh are good friends"
print(s.rsplit(' ',1))

'''


#index
'''
s=input("enter")
sub=input("enter thw substring")
strt=int(input("enter the stat-index"))
print(s.index(sub,strt))

output:enterpavankumar
enter thw substringa
enter the stat-index4
8

#2 method
s=input("enter")
sub=input("enter thw substring")
print(s.index(sub))

output:enterpavankumar
enter thw substringar
8
'''
#find is same as index but the difference is if you give the unkown sunstring itd prints the -1
'''
s=input("enter")
sub=input("enter thw substring")
strt=int(input("enter the stat-index"))
print(s.find(sub,strt))


#2 method
s=input("enter")
sub=input("enter thw substring")
print(s.index(sub))


output:enterpavan
enter thw substringq
enter the stat-index2
-1
'''


#count
'''
s="good morning mam"
print("enter the o's",s.count('o'))
print(s.count("123"))   #default value of string is " " in this cse we use count so its 0
print(s.count('o',2))   #its starts from 2 and counts the no.of "o" in the string

output:3
0
2

'''
#strip #removes the given characters
'''
s=input("enter :\n")
char=input("enter the char")
print(s.strip(char))



output:enter :
pavan is good3
pavan
 is good3

2.kiwi fruit
ifrtuk
wi
3.enter :
i am good
doig
 am
'''
# Lstrip
'''
s=input("enter :\n")
char=input("enter the char")
print(s.lstrip(char))

output:
    enter :
i am good
enter the chari i a
m good


enter :
i am good
enter the chari a d
m good


'''

#rstrip()
'''
s=input("enter :\n")
char=input("enter the char")
print(s.rstrip(char))


output:
enter :
i am good
enter the charujid0
i am goo


enter :
i am good
enter the chareioejrdoo
i am g

enter :
i am good
enter the charavod
i am g

'''


s="i am good"
print(s.rstrip("o,d"))
print(s.rstrip("m,o,d"))

#Reverse a string
'''
a=input()
print(a[::-1])
'''



#Substring of a given string

'''
a=input()
for i in range(0,len(a)-2):
    print(a[i:i+3])

output:india
ind
ndi
dia
'''



#first latter and last letter
'''
a=input()
print(a[1:len(a)-1])
'''

#reverse a string except first and last characters

'''
a=input()
print(a[len(a)-2:0:-1])

output:avankuma
'''

#palindrom
'''
a=input()
b=a[::-1]
if(b==a):
    print("Given string is palindrom")
else:
    print("given string is not  palindrom")
'''



#Comparing two strings
'''
a="pavan"
b="pavan"
if(a==b):
    print("two strings are equal")
else:
    print("two strings are  not equal")
'''


'''
a=["python","java","django","spring"]
b=len(a)
for i in range(0,b):
    s=""
    for j in range(i+1):
        s=s+str(a[j])
    print(s,sep=", ")

output:python
pythonjava
pythonjavadjango
pythonjavadjangospring
  

'''


#to change the string into uppercase
'''
a=input()
s=""
for i in a:
    if(ord(i)>=97 and ord(i)<=122):
        s=s+chr(ord(i)-32)
print(s)
output:PAVAN
'''


#join()
'''
a=["python","java","Django","spring"]
s="".join(a)
print(s)

output:python java Django spring
'''
'''
url=["https://www.google.com","https://www.amazon.com","http://www.flipkart.com"]
for i in url:
    if(i[0:5]=="https"):
        print(i)
        
'''




'''
s=["https://www.google.com/","https://www.amazon.com","http://www.flipkart.org"]
for i in s:
    if(i.endswith(("com","com/"))):
        print(i)
'''


#To check the string how many upper,lower,number and special characters count without using built in functions
'''
a=input()
lower=0
upper=0
number=0
special=0
for i in a:
    if(ord(i)>=97 and ord(i)<=122):
        lower=lower+1
    elif(ord(i)>=65 and ord(i)<=97):
        upper=upper+1
    elif(ord(i)>=48 and ord(i)<=57):
        number=number+1
    else:
        special=special+1
print(lower,upper,number,special)

output:pavANK@!$630
lower case: 3
upper case: 3
number: 3
special : 3
'''


#To check the string how many upper,lower,number and special characters count using builtin functions
'''
a=input()
lower,upper,number,special=0,0,0,0
for i in a:
    if(i.islower()):
        lower=lower+1
    elif(i.isupper()):
        upper+=1
    elif(i.isnumeric()):
        number+=1
    else:
        special+=1
print("lower case:",lower)
print("upper case:",upper)
print("number:",number)
print("special :",special)   
'''

#Swapcase and title
'''
s=input()
s1=s.swapcase()
s2=s.title()
print(s)
print(s1)
print(s2)

output:PAvAN
p a V a n 

'''
#converting a string to loer case to uppercase and vice versa(without using swapcase)
'''
s=input()
a=""
c=0
d=0
for i in s:
    if(ord(i)>=65 and ord(i)<=96):
        a+=chr(ord(i)+32)
        c+=1
    else:
        a+=chr(ord(i)-32)
        d+=1
print(a ,end=" ") 
print("upperCount:",d)
print("lowercount:",c)

output:pAvAn
PaVaN upperCount: 3
lowercount: 2
'''


# To convert vowels to uppercase and remove the digits from the given string
'''
s=input()
a=s.lower()
num="012345678"
b=""
for i in a:
    if(i in ("aeiou")):
        b=b+i.upper()
    elif(i not in num):
        b=b+i    
print(b)output:Error 404 page not found
ErrOr  pAgE nOt fOUnd
'''

#using maketrans
#To convert vowels to uppercase and remove the digits from the given string
'''
s=input()
table=s.maketrans("aeiou","AEIOU","0123456789")
s_table=s.translate(table)
print(s_table)

output:error page 404 not found
ErrOr pAgE  nOt fOUnd
'''

#format(,)
'''
a=input("enter the name:")
b=input("enter the place:")
s="hello {},How is the weather in {}?".format(a,b)

output:hello pavan,How is the weather in benguluru?
'''

# format left allignment

s="{0:*<10}".format(999)
#output:999*******

'''
#right alignment
s="{0:*>10}".format(999)
print(s)
#output:*******999


#center allignment
s="{0:*^10}".format(999)
print(s)
#output:***999****
'''


#.f format
'''
import math
s="{0:.4f}".format(math.pi)
print(s)

output:3.1416

import math
s="{0:#>10.4f}".format(math.pi)
print(s)

output:####3.1416
'''

#exponential format
'''
ew=597600000000000000000000
s="{0:e}".format(ew)
print(s)
4
#output:5.976000e+23

ew=597600000000004
0000000000
s="{0:.3e}".format(ew)
print(s)

output:5.976e+23


ew=597600000000000000000000
s="{0:@>20.3e}".format(ew)
print(s)

output:@@@@@@@@@@@5.976e+23

'''

'''
s="{},{},{}".format([10,20,30])
print(s)

#output :index 1 out of range for positional args tuple because in list having 3 values that is 10,20,30 but in format condition by default it takes as tuple so the index is 0
'''
'''
s="{}".format([10,20,30])
print(s)
output:[10, 20, 30]
'''
'''
s="{}".format(*[10,20,30])
print(s)
output: 10 #because we acesss only one values({}) in list


s="{},{},{}".format(*[10,20,30])
print(s)

output:10,20,30
#by using * operation in format it unpack the values in the list
'''








'''
s1,s2="hi guys","how are you"
print(s1,s2 ,sep="\n")




#constructor: str()
#1.
print(type(s3))
#default value: ' ' or " "
print(str())
#typecasting

i,f,c,b=str(1),str(2.2),str(3+4j),str(True)
print(type(i),i)
print(type(i),f)
print(type(i),c)
print(type(i),b)
'''
'''
s=input("enter the string:")
print("string : ",s,"It is the length is:",len(s))
'''



'''
s="bangolre"
print(s,len(s))

print(s[1],s[4])

print(s[1],s[len(s)-1])
print(id(s[1]),id(s[4]))
'''



'''
a=input()
b=len(a)//2
print(a[b])
'''
'''
a=input()
b=len(a)-2
print(a[b])
'''

'''
s=input()
print(s[:3])
'''

'''
print(float("2.5"))
print(int(2+0j))
'''

'''
s="welcome to my channel"
print(s)
print(s[::])
print(s[1::2]) #odd values
print(s[::2])#even values
print(s[:7:2])#in welcome we take even values
print(s[1:7:2])# in welcome we take odd values

output:welcome to my channel
welcome to my channel
ecm om hne
wloet ycanl
wloe
ecm
'''


#s="welcome to my channel"
'''
print(s[::-1])
print(s[len(s)-1:12:-1])
print(s[-1:-8:-1])


print(s[:10])
print(s[10::-1])
print(s[-12::-1])
print(s.index("t"))
print(s[12:7:-1])

'''
#for i in range(len(s)):
    
'''   
#print(s[-9:-14:-1])
s="slicing is tricky"
print(s)
print(len(s))
print(s[::-1])
print(s[6::-1])
print(s[-11::-1])
print(s[9:7:-1])
print(s[-8:-10:-1])
print(s[len(s)-1:10:-1])
print(s[-1:-7:-1])
print(s[12:3:-1])
print(s[-5:-14:-1])
'''
'''
s="welcomec"
a=len(s)
for i in range(a):
    if(s[i]=="c"):
        print(i)
'''
'''
a=0
b=1
for i in range(10):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
        
'''

'''
s="welcome to my channel"
print(s[len(s)-2::-2])#skip even index means odd index
print(s[len(s)::-2])#skip odd index means even char

output:-enh mo mce
lnacy teolw
'''
s="welcome to my channel"
'''
print(s[6::-1])#emoclew
print(s[6::-2])#eolw
print(s[5::-2])#mce
'''
'''
#to my
print(s[12:7:-1])#ym ot
print(s[12:7:-2])#y t
print(s[11:7:-2])#mo

#to my negative index
print(s[-8:-14:-2])
'''


'''
#replace


a="Hello world"
print(a.replace("l","L"))
print(a.replace("Hello","Hai"))#Hai world
print(a.replace("l","L",1))
print(a.replace(a[3],"L"))
print(a.replace("o","@",1))#Hell@ world
print(a.replace("o","@",2))#Hell@ w@rld
a="Hello world"
print(a.replace(a[4],"L"))
'''

'''
#lower()
a=input("enter the string: \n")
print(a.lower())
OUTPUT:enter the string: 
pAVA@23
pava@23
'''
'''
a="pavan kumar"
b=a.replace(a[6:],"KUMAR")
print(b)
'''
'''
a=input("enter the string:\n")
print(a.islower())

a=input("enter the string:\n")
print(a.isupper())

a=input("enter the string:\n")
print(a.isalpha())

a=input("enter the string:\n")
print(a.isalpha())
'''
a=input("enter the string:\n")
print(a.isalnum())

output:enter the string:
qwe12@
False





'''
print(89)
print(5.6,sep="@")
print(3,4,end="*"
)
'''

#startswith()   its only acess index it cannot acess slicing
'''
str1=input("enter")
sub_s=input("substring")
starts=int(input("enter the value"))
print(str1.startswith(sub_s,starts))

output:enterpavan
substringa
enter the value3
True
'''


#endswith()  its only acess index it cannot acess slicing
'''
str1=input("enter:\n")
sub_s=input("substring:\n")
ends=int(input("enter the value:\n"))
#print(str1.endswith(sub_s,0,ends))
print(str1.endswith(sub_s,-1,ends))


output:enter:           
pavan
substring:
a
enter the value:
4
True

enter:
pavan
substring:
a
enter the value:
-2
False

enter:
pavan
substring:
a
enter the value:
-3
True
'''
'''
s="pavan"
print(s.endswith())
'''


'''
s="pavan and jagadeesh are good friends"
print(s.split())  #['pavan', 'and', 'jagadeesh', 'are', 'good', 'friends']
print(s.split("and"))  #['pavan ', ' jagadeesh are good friends']
print(s.split("are"))  #['pavan and jagadeesh ', ' good friends']
print(s.split("a",1))  #['p', 'van and jagadeesh are good friends']
s="pavan-jagadeesh-good friends"
print(s.split("-",1))#['pavan', 'jagadeesh-good friends']
#rsplit
s="pavan and jagadeesh are good friends"
print(s.rsplit(' ',1))

'''


#index
'''
s=input("enter")
sub=input("enter thw substring")
strt=int(input("enter the stat-index"))
print(s.index(sub,strt))

output:enterpavankumar
enter thw substringa
enter the stat-index4
8

#2 method
s=input("enter")
sub=input("enter thw substring")
print(s.index(sub))

output:enterpavankumar
enter thw substringar
8
'''
#find is same as index but the difference is if you give the unkown sunstring itd prints the -1
'''
s=input("enter")
sub=input("enter thw substring")
strt=int(input("enter the stat-index"))
print(s.find(sub,strt))


#2 method
s=input("enter")
sub=input("enter thw substring")
print(s.index(sub))


output:enterpavan
enter thw substringq
enter the stat-index2
-1
'''


#count
'''
s="good morning mam"
print("enter the o's",s.count('o'))
print(s.count("123"))   #default value of string is " " in this cse we use count so its 0
print(s.count('o',2))   #its starts from 2 and counts the no.of "o" in the string

output:3
0
2

'''
#strip #removes the given characters
'''
s=input("enter :\n")
char=input("enter the char")
print(s.strip(char))



output:enter :
pavan is good3
pavan
 is good3

2.kiwi fruit
ifrtuk
wi
3.enter :
i am good
doig
 am
'''
# Lstrip
'''
s=input("enter :\n")
char=input("enter the char")
print(s.lstrip(char))

output:
    enter :
i am good
enter the chari i a
m good


enter :
i am good
enter the chari a d
m good


'''

#rstrip()
'''
s=input("enter :\n")
char=input("enter the char")
print(s.rstrip(char))


output:
enter :
i am good
enter the charujid0
i am goo


enter :
i am good
enter the chareioejrdoo
i am g

enter :
i am good
enter the charavod
i am g

'''


s="i am good"
print(s.rstrip("o,d"))
print(s.rstrip("m,o,d"))


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

