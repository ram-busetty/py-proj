# n1=int (input("enter a number:"))
# n2=int (input("enter a number:"))
# n3=int (input("enter a number:"))
# if n1>n2 and n1>n3:
#     print("n1 is greater",n1)
# elif n2>n3:
#     print("n2 is greater",n2)
# else:
#     print("n3 is greater",n3)

# ===============================================
# ch=input("enter a character:")
# if ch.isupper():
#     print(ch.lower())
# elif ch.islower():
#     print(ch.upper())
# elif '0'<=ch<='9':
#     print(int(ch)%3)
# else:
#     print("it is aspecial character",ord(ch))


# ================================================================
# n1=int(input("enter the number:"))
# n2=int(input("enter the number:"))
# if n1>0 and n2>0:
#     print("quadrant 1")
# elif n1<0 and n2>0:
#     print("quadrant 2")
# elif n1<0 and n2<0:
#     print("quadrant 3")
# elif n1!=0 and n2==0:
#     print(f'x-axis{(n1,n2)}')
# elif n1==0 and n2!=0:
#     print(f'y-axis{(n1,n2)}')
# else:
#     print("quadrant 4")



# =================================================================

# num=int(input("enter a number:"))
# sum=0
# for i in range(2):
#     n1=num%10
#     sum=sum+(n1*10)
#     num=num//10
#     print(num)
# print(sum)




# ========================================================================
# target=2
# beg=int(input("enter the beggining"))
# end=int(input("enter the end number"))
# i=beg
# while i>=beg and i<=end:
#     j=1
#     count=0
#     temp=0
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         temp+=1
#     if target == temp:
#         print(i)
#     i+=1

# ================================================
# extracting the prime number from  a number
# n=23576
# while n>0:
#     temp=n%10
#     j=1
#     i=temp
#     count=0
#     while j<=i:
#         if i%j==0:
#             count=count+1
#         j=j+1
#     if count==2:
#         print(i)
#     n=n//10

# ======================================================================
#  second prime number in the given range
# beg=int(input("enter the beggining number:")) 
# end=int(input("enter the ending number:")) 
# target=int(input("enter the target:"))
# i=beg
# temp=0
# while i>=beg and i<=end:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         temp+=1
#     if temp==target:
#         print("the nth prime number:",i)
#         break
#     i+=1
# ============================================================================
# to find the nth prefect number
# beg=1
# end=10000
# i=beg
# target=4
# temp=0
# while i>=beg and i<=end:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0 and j!=i:
#             count+=j
#         j+=1
#     if count==i:
#         temp+=1
#     if target==temp:
#         print("the nth perfect number:",i)
#         break
#     i+=1
# ============================================================================
# find the  sum of perfect numbers in the given range
# beg=int(input("enter the begining number::"))
# end=int(input("enter the ending number:"))
# i=beg
# sum=0
# while i>=beg and i<=end:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0 and j!=i:
#             count+=j
#         j+=1
#     if count==i:
#         print("the perfect numbers in the given range:",count)
#         sum+=i
#     i+=1
# print("the sum of the perfect numbers in the given range",sum)
# ============================================================================
# print the perfect number in the given range
# beg=int(input("enter the begining number:"))
# end=int(input("enter the ending number:"))
# i=beg
# while i>=beg and i<=end:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0 and j!=i:
#             count+=j
#         j+=1
#     if count==i:
#         print("the perfect numbers in the given range:",i)
#     i+=1
# ============================================================================
# print the  nth fibonocci number in the given range
# range=10
# prev=0
# next=1
# target=int(input("enter the target:"))
# i=1
# while i<=range :
#     if i==target:
#          print(prev)
#     fib=prev+next
#     prev=next
#     next=fib
#     i+=1

# ============================================================================
# 1.peterson number
# number=int(input("enter the number:"))
# n1=number
# temp=0
# while number>0:
#      digit=number%10
#      sum=1
#      while digit>0:
#           sum=sum*digit
#           digit-=1
#      temp+=sum
#      number//=10
# if n1==temp:
#      print("the number is peterson number:",n1)
# else:
#      print("not a peterson number:",n1)
# ============================================================================
# sunny number
# n=int(input("enter the number:"))
# n1=n+1
# i=2
# while i<=n:
#     if (i**2)==n1 and (i**2)<=n1:
#         print(f"sunny number number:{i}")
#         exit()
#     if (i**2)>n1:
#         print(f"not a sunny number:{i}")
#         exit()
#     i+=1
# ============================================================================
# tech number
# number=int(input("enter a number:"))
# n1=number
# n2=number
# count=0
# while number>0:
#     count+=1
#     number=number//10
# sum=0
# if count%2==0:
#     while n1>0:
#         temp=n1%100
#         sum+=temp
#         n1//=100
#     sum**=2
#     if sum==n2:
#         print(f"tech number{n2}")
#     else:
#         print(f"not a tech number{n2}")
# else:
#     print("even digit number:")

# ============================================================================
# ============================================================================
# ============================================================================

# splitting the number into nth parts
# n=int(input("enter the number:"))
# target=int(input("enter the target:"))
# splitter=1
# while target>0:
#     splitter*=10
#     target-=1
# print(splitter)

# ============================================================================
# ============================================================================
# ============================================================================
# number=int(input("enter a prime number:"))
# number=97
# n1=number
# rev=0
# while n1>0:
#     digit=n1%10
#     rev=rev*10+digit
#     n1=n1//10


# i=1

# count=0
# while i<=number:
#     j=1
#     if i%j==0:
#         count+=1
#     j+=1
# if count==2:
#     print("the given number is prime number:")

# ============================================================================
# ============================================================================
# ============================================================================

# spy numer
# beg=100
# end=200
# for i in range(beg,end+1):
#     temp=i
#     prod=1
#     sum=0
#     # print(i)
#     while temp>0:
#         digit=temp%10
#         sum+=digit
#         prod*=digit
#         # print(digit)
#         temp//=10
#     if sum==prod:
#         print(i)

# ============================================================================
# ============================================================================
# ============================================================================
#  nth strong number
# beg=int(input("enter  beggining number:"))
# end=int(input("enter the ending number:"))
# target=int(input("enter the target:"))
# count=0
# for i in range(beg,end+1):
#     temp=i
#     sum=0
# while temp>0:
#     digit=temp%10
#     fact=1
#     if digit==0:
#         fact=1
        
#     while digit>0:
#         fact=fact*digit
#         digit-=1
#     sum=sum+fact
#     temp//=10
#     if sum==i:
#         # print(i)
#         count+=1
#         if count==target:
#             print(f"the {target}strong number is{i}")
            
# ============================================================================
# ============================================================================
# ============================================================================
# beg=int(input("enter  beggining number:"))
# end=int(input("enter the ending number:"))
# for i in range(beg,end+1):
#     temp=i
#     sum=0
#     while temp>0:
#         digit=temp%10
#         fact=1
#         if digit==0:
#             fact=1
        
#         while digit>0:
#             fact=fact*digit
#             digit-=1
#         sum=sum+fact
#         temp//=10
#     if sum==i:
#         print(i)
# ============================================================================
# ============================================================================
# ============================================================================
# odd indexed characters
# s=input("enter the  string:")
# for i in range(len(s)):
#     if i%2==1:
#         if s[i]>='a'and s[i]<='z'or s[i]>='A'and s[i]<='Z':
#             print(f"the odd indexed characters are:{s[i]}")
# ============================================================================
# ============================================================================
# ============================================================================
# even indexed lowercase alphabets
# s=input("enter a string:")
# for i in range(len(s)):
#     if i%2==0:
#         if s[i]>='a'and s[i]<='z':
#             print(f"the lowercase alphabets are:{s[i]} ")
# ============================================================================
# ============================================================================
# ============================================================================
# tech number(2025 → (20+25)² = 45² = 2025)
# number=int(input("enter a number:"))
# n1=number
# n2=number
# count=0
# while number>0:
#     count+=1
#     number=number//10
# if count%2==0:
#     splitter=count//2
#     initial=1
#     while splitter>0:
#         initial=initial*10
#         splitter-=1
#     sum=0
#     while n1>0:
#         temp=n1%initial
#         sum+=temp
#         n1//=initial
#     sum**=2
#     if sum==n2:
#         print(f"tech number:{n2}")
#     else:
#         print(f"not a tech number:{n2}")
# ============================================================================
# ============================================================================
# ============================================================================
# count=6
# if count%2==0:
#     splitter=count//2
#     initial=1
#     while splitter>0:
#         initial=initial*10
#         splitter-=1
#     print(initial)
# ============================================================================
# ============================================================================
# ============================================================================
# Automorphic number 
# * 5 → 5² = 25 → ends with 5
# * 25 → 25² = 625 → ends with 25
# number=int(input("entr a number:"))
# n1=number
# count=0
# square_number=number**2
# print(square_number)
# while number>0:
#     count+=1
#     number//=10
# initial=1
# while count>0:
#     initial=initial*10
#     count-=1
# if square_number%initial==n1:
#     print(f"the given number is the automorphic number:{n1}")
# else:
#     print(f"the given number is not automorphic number:{n1}")
# ============================================================================
# ============================================================================
# ============================================================================
# keith number
# number=int(input("enter a number:"))
# n1=number
# sum=0
# last=n1%10
# while n1>0:
#     digit=n1%10
#     sum+=digit
#     n1//=10
# keith=sum+last
# if number == keith:
#     print(f"the number is keith{number}")
# last=sum



# ============================================================================
# ============================================================================
# ============================================================================

# s = input("")
# res = ''
# count = 1

# for i in range(len(s)):
#     if s[i] not in 'aeiouAEIOU':
#         res += s[i]
#         count = 1
#     else:
#         res = res + s[i] + str(count)
#         count += 1

# print(res)
# ============================================================================
# ============================================================================
# ============================================================================
# s=input("enter a string:")
# res=''
# for i in s:
#     if i not in res:
#         res+=i
# print(res)
# l=[]
# for i in range(len(res)):
#     count=0
#     for j in range(len(s)):
#         if res[i]==s[j]:
#             count+=1
#     l.append(count)
# print(l)


# ============================================================================
# ============================================================================
# ============================================================================
# s=input("enter a character:")

# for i in range(len(s)):
#     for j in range(len(s)):
#         k=i
#         res=''
#         while k<=j:
#             res+=s[k]
#             k+=1
#         if len(res)>1 and res[::]==res[::-1]:
#             print(res)
# ============================================================================
# ============================================================================
# ============================================================================

# def palindrome_num(n,n1):
#     rev=0
#     while n1>0:
#         digit=n1%10
#         rev=rev*10+digit
#         n1=n1//10
#     if rev==n:
#         print(f"the palindrome is: {n}")
#     else:
#         updated=n+rev
#         print(updated)
#         updated1=updated
#         palindrome_num(updated,updated1)
# number=int(input("enter a number:"))
# n1=number
# palindrome_num(number,n1)

# ============================================================================
# ============================================================================
# ============================================================================
# s=input("enter a string:")
# for i in range(len(s)-1):
#     count=0
#     j=0
#     while j< len(s):
#         if s[i]==s[j]:
#             count+=1
#         j+=1
#     if count==1:
#         print(s[i])
#         exit()
# ============================================================================
# ============================================================================
# ============================================================================
# s=input("enter a string:")
# res=''
# res1=''
# for i in range(len(s)):
#     if s[i] in 'aeiouAEIOU':
#         res+=s[i]
#     elif s[i] not in'aeiouAEIOU':
#         res1+=s[i]
# print(f"the vowels{res},the consonants{res1}")
# ============================================================================
# ============================================================================
# ============================================================================
# s=input("enter a string:")
# res=''
# res1=''
# num=''
# for i in range(len(s)):
#     if s[i] not in 'aeiouAEIOU' and s[i] not in '0123456789':
#         res+=s[i]
#     elif s[i] in 'aeiouAEIOU':
#         res1+=s[i]
#     elif '0'<=s[i]<='9':
#         num+=s[i]
# print(f"the consonants:{res}the vowels:{res1}the numbers:{num}",end='\n')
# ============================================================================
# ============================================================================
# ============================================================================
# s=input("enter string:")
# spc=''
# num=''
# vow=''
# con=''
# for i in range(len(s)-1,-1,-1):
#     # print(s[i])
#     if not ('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9'):
#        spc+=s[i]
#     elif '0'<=s[i]<='9':
#         num+=s[i]
#     elif s[i] in 'aeiouAEIOU':
#         vow+=s[i]
#     elif s[i] not in 'aeiouAEIOU' and 'a'<=s[i]<='z' or 'A'<=s[i]<='Z':
#         con+=s[i]
# print(spc+','+num+','+vow+','+con)   
# (*12hello3$ $4#world4*) 
# ============================================================================
# ============================================================================
# ============================================================================
# s=input("enter string:")
# spc=''
# num=''
# vow=''
# con=''
# for i in range(len(s)):
#     # print(s[i])
#     if not ('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9'):
#        spc+=s[i]
#     elif '0'<=s[i]<='9':
#         num+=s[i]
#     elif s[i] in 'aeiouAEIOU':
#         vow+=s[i]
#     elif s[i] not in 'aeiouAEIOU' and 'a'<=s[i]<='z' or 'A'<=s[i]<='Z':
#         con+=s[i]
# print(con+','+vow+','+num+','+spc)   
# ============================================================================
# ============================================================================
# ============================================================================
# (*12hello3$ $4#world4*)
# ,hllwrld,)*#$ $*(,eoo,44321
 
# s=input("enter string:")
# spc=''
# num=''
# vow=''
# con=''
# for i in range(len(s)):
#     # print(s[i])
#     if s[i] in 'aeiouAEIOU':
#         vow+=s[i]
#     elif s[i] not in 'aeiouAEIOU' and ('a'<=s[i]<='z') or ('A'<=s[i]<='Z'):
#         con+=s[i]
   
   
# for i in range(len(s)-1,-1,-1):
#     if not ('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9'):
#        spc+=s[i]
#     elif '0'<=s[i]<='9':
#         num+=s[i]

# print(','+con+','+spc+','+vow+','+num)   
# ============================================================================
# ============================================================================
# ============================================================================
# s=input("enter string:")
# spc=''
# num=''
# vow=''
# con=''
# for i in range(len(s)-1,-1,-1):
#     # print(s[i])
#     if not ('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9'):
#        spc+=s[i]
#     elif '0'<=s[i]<='9':
#         num+=s[i]
#     elif s[i] in 'aeiouAEIOU':
#         vow+=s[i]
#     elif s[i] not in 'aeiouAEIOU' and 'a'<=s[i]<='z' or 'A'<=s[i]<='Z':
#         con+=s[i]
# print(str(con+spc+vow+num))
# ============================================================================
# ============================================================================
# ============================================================================
    # l=list(input("enter a list:"))
    # for i in range(len(l)-1):
    #     count=0
    #     for  j in range(len(l)):
    #         if l[i]==l[j]:
    #             count+=1
    #     if count>1:
    #         l.remove(l[i])

# ============================================================================
# ============================================================================
# ============================================================================
# l = list(input("enter a list:"))
# res=[]
# for i in range(len(l)):
#    if l[i] not in res:
#       res.append(l[i])
# print(res)
# ============================================================================
# ============================================================================
# ============================================================================
# l = list(input("enter a list:"))
# l1=[]
# l2=[]
# for i in range(0,len(l)//2):
#     l1.append(l[i])
# for i in range(len(l)//2,len(l)):
#     l2.append(l[i])
# print(l1,l2)
# ============================================================================
# ============================================================================
# ============================================================================
#  fascinating number:
# number=int(input("enter a number:"))
# sum=number+(number*2)+(number*3)
# count=0
# s=str(sum)
# print(s,type(s))
# print(sum)
# for i in range(10):
#     print(i)
#     if i in s:
#         count+=1
# if count==10:
#     print(sum)
# else:
#     print(f"not a fasinating number:{sum}")
# ============================================================================
# ============================================================================
# ============================================================================
# l=[1,2,3,4,5]
# l1=[2,3,4,5,6]
# l3=[]
# for i in l:
#     if i in l1:
#         l3+=[i]
# print(l3)
# ============================================================================
# ============================================================================
# ============================================================================
# l=['Jspiders@','PySpiders#','Qspiders$']
# l1=[]
# for i in l:
#     for j in i:
#         if not('A'<=j<='Z' or'a'<=j<='z'or '0'<=j<='9'):
#             l1+=[j]
# print(l1)
# ============================================================================
# ============================================================================
# ============================================================================
# l=['Jspiders@','PySpiders#','Qspiders$']
# l1=[]
# for i in range(len(l)):
#     for  j in range(len(l[i])):
#         if 'A'<=l[i][j]<='Z':
#             l1+=[l[i][j]]
# print(l1)
# ============================================================================
# ============================================================================
# ============================================================================

# ============================================================================
# ============================================================================
# ============================================================================
# l=[1,2,3,4,5,6,7,8,9]
# l1=[]
# number=int(input("enter a number:"))
# n1=number
# n_2=number*2
# n_3=number*3
# concat_number=int(str(number)+str(n_2)+str(n_3))
# print(concat_number,type(concat_number))
# temp=concat_number
# print(temp)
# while temp>0:
#     digit=temp%10
#     l1+=[digit]
#     temp//=10
# print(l1,l)
# if l==sorted(l1):
#     print(f'the given numbetr:{n1} and it is fascinating number:{concat_number} ')
# else:
#     print(f'the given number:{n1} and it is not a fascinating number:{concat_number}')
# ============================================================================
# ============================================================================
# ============================================================================
# s='hi hello '
# res=''
# l=[]
# for i in range(len(s)):
#     if s[i]!='':
#         res+=s[i]
#     else:
#         l+=[res]
#         res=''
# print(l)
# ============================================================================
# ============================================================================
# ============================================================================
# for i in range(1,8):
#     for j in range(1,6):
#         if ((j==2 or j==3 or j==4 )and i==1) or (j==1 and i>0) or (i==4 and j!=5 ) or ((i==2 or i==3) and j==5)or ((i==5 or i==6)and j==5 ) or (i==7 and(j==2 or j==3 or j==4)):
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# ============================================================================
# ============================================================================
# ============================================================================
# for i in range(1,5):
#     for j in range(4-i):
#         print(' ',end=' ')
#     for k in range(1,i*2):
#         print('*',end=' ')
#     print()
# ============================================================================
# ============================================================================
# ============================================================================
# for i in range(0,5):
#     k=5
#     for j in range(k-i):
#         print('*',end=" ")  
#     print()
    # op:-
        # * * * * * 
        # * * * * 
        # * * * 
        # * * 
        # *

# ============================================================================
# ============================================================================
# ============================================================================
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(i):
#         print('*',end=" ")
    # print()
    # op:-
    # * 
    # * * 
    # * * * 
    # * * * * 
    # * * * * * 
    # * * * * 
    # * * * 
    # * * 
    # *
# ============================================================================
# ============================================================================
# ============================================================================
# for i in range(1,6):
#     k=5
#     for j in range(k-i):
#         print(' ',end=' ')

#     for k in range(i):
#         print('*',end=" ")
#     print()
# for i in range(1,6):
#     k=5
#     for s in range(i):
#         print(' ',end=' ')
#     for j in range(k-i):
#         print("*",end=' ')
#     print()
# op:-
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         *    
# ============================================================================
# ============================================================================
# ============================================================================
    # *  *  *  *  *
    #   *  *  *  *
    #     *  *  *
    #       *  *
    #         *

# ============================================================================
# ============================================================================
# ============================================================================
# def pal(s):
#     if s== s[::-1]:
#         print(f'given string is a palindrome:{s}')
#     else:
#         print(f'Given string is not a palindrome:{s}')
# pal('ram')
# ============================================================================
# ============================================================================
# ============================================================================
# def max(*args):
#     max=0
#     for i in args:
#         if i>max:
#             max=i
#     return max
# print(max(1,3,5))
# ============================================================================
# ============================================================================
# ============================================================================
# def student_details(*args,**kwarg):
#     print(f'positional arguments{args}')
#     print(f'keyword positional arguments{kwarg}')
# print(student_details('maths','physics',name='ram',age=20,loc='hyd'))
# ============================================================================
# ============================================================================
# ============================================================================
# def areaOfRectangle(length,breadth=2):
#     return f'Area of rectangle:{length*breadth}'
# print(areaOfRectangle(5))
# ============================================================================
# ============================================================================
# ============================================================================
# balance=10000
# def bankaccount():
#     def deposit(amount):
#         global balance
#         balance+=amount
#         return balance
#     def withdrawl(amount):
#             global balance
#             if amount<= balance:
#                 balance-= amount
#                 return balance
#             else:
#                 print("insufficient balance:")
#     def bal():
#         return balance
#     print(f'depasited amount-->{deposit(1000)}')
#     print(f'remainning balance after withdrawl-->{withdrawl(999)}')
#     print(f'remainning balance-->{bal()}')
# bankaccount()
# ============================================================================
# ============================================================================
# ============================================================================
# class bike:
    #creation of class varables
#     bikeName='kwasaki'
#     bikeno=8690
# bike.bikeColor='green'
# bike.bikeModel='H2r'
# b1=bike()
# b2=bike()
# b3=bike()
#accessing the class varables
# print (b1.bikeName,b1.bikeno,b1.bikeColor,b1.bikeModel)
# print (b2.bikeName,b2.bikeno,b2.bikeColor,b2.bikeModel)
# print (b3.bikeName,b3.bikeno,b3.bikeColor,b3.bikeModel)
# updating the class varables
# b1.bikeName='bugatti' 
# print(b1.bikeName,b2.bikeName)
# bike.bikeno=8686
# print(b1.bikeno,b2.bikeno,b3.bikeno)

#deleting the class variable
# del bike.bikeColor
# print(b1.bikeName,b1.bikeno,b1.bikeModel)

# print(bike.__dict__)
# ============================================================================
# ============================================================================
# ============================================================================
class mobile:
    mobileName=None
    mobilePrice=None
m1=mobile()
m1.mobileColor='black'
m1.mobileRAM='126GB'
m1.mobileSize='13inch'
m1.mobileName='moto'
m1.mobilePrice=120000
# print(mobile.__dict__)
# reading the object variables
print(m1.mobileName,m1.mobilePrice,m1.mobileColor,m1.mobileRAM,m1.mobileSize)
# updating the object variables
m1.mobileName='iphone'
print(m1.mobileName)
#deleting the objectVariables
# del m1.mobleSize
# print(m1.mobileSize)

m2=mobile()
m2.mobileName='samsung'
m2.mobilePrice=100000
m2.mobileColor="jetBlack"
m2.mobileRAM='12GB'
m2.mobileSize='10inch'

print(m2.mobileName,m2.mobilePrice,m2.mobileColor,m2.mobileRAM,m2.mobileSize)
# ============================================================================
# ============================================================================
# ============================================================================

class laptop:
    laptopName=None
laptop.laptopPrice=None
l1=laptop()
l2=laptop()
l2.laptopColor='pink'
l1.laptopModel='m1Air'
l1.laptopRAM='16GB'
l1.laptopSize='13.3inch'
l1.laptopColor='grey'
#  Accessing varaibles
print(l1.laptopName,l1.laptopPrice,l1.laptopModel,l1.laptopRAM,l1.laptopSize,l1.laptopColor)
# updating the varables
l1.laptopName='Macbook'
print(l1.laptopName,l1.laptopPrice,l1.laptopModel,l1.laptopRAM,l1.laptopSize,l1.laptopColor)
# del l1.laptopColor
print(l1.laptopColor,l2.laptopColor)
# ============================================================================
# ============================================================================
# ============================================================================
class movie:
    movieName='none'
    movieBudjet='none'
m1=movie()
m1.movieName='Dune'
m1.movieBudjet='10000cr'
m1.hero='paul'
movie.heroine='chani'
m1.duration='3hrs'
# reading values
print(m1.movieName,m1.movieBudjet,m1.hero,m1.heroine,m1.duration)
# upating values
movie.heroine='zendaya'
print(m1.heroine)
# del m1.duration
print(m1.movieName,m1.movieBudjet,m1.hero,m1.heroine,m1.duration)
# ============================================================================
# ============================================================================
# ============================================================================
class car:
    carName=None
    carPrice=None
c1=car()
car.carPrice=12000000
c1.carName='Lamborgini'
c1.carColor="JetBlack"
c1.exhaustType='Dual'
c1.carModel='XX01H2'
print(c1.carName,c1.carPrice,c1.carColor,c1.exhaustType,c1.carModel)
c2=car()
c2.carName='buggati'
c2.carPrice=10000000
c2.carColor='vintageBlack'
c2.exhaustType='Dual'
c2.carModel='XRPO11'
print(c2.carName,c2.carPrice,c2.carColor,c2.exhaustType,c2.carModel)
c2.carName='ferrari'
print(c2.carName)
del c2.carName
print(c2.carName)
# ============================================================================
# ============================================================================
# ============================================================================
class bank:
    def initialize(self,name,accno,balance):
        self.name=name
        self.accno=accno
        self.balance=balance
    def display(self):
        print(self.name,self.accno,self.balance)
b1=bank()
b1.initialize('SBI','TPY001',100000)
b1.display()
b2=bank()
bank.initialize(b2,'ICICI','PPYT001',1000000)
bank.display(b2)
# ============================================================================
# ============================================================================
# ============================================================================
class movie:
    def __init__(self,movieName,hero,heroine):
        self.movieName=movieName
        self.hero=hero
        self.heroine=heroine
    def getinfo(self):
        print(self.movieName,self.hero,self.heroine)
m1=movie('dune','paul','chani')
m1.getinfo()


class Bank:
    def __init__(self,Name,balance=5000):
        self.Name=Name
        self.Balance=5000
    def displayBalance(self):
        print(self.Balance)
    def deposit(self,amount):
        if amount>0:
            self.Balance+=amount
    def withdrawl(self,cash):
        if cash <= self.Balance:
            self.Balance-=cash
b1=Bank("Prasanth")
b1.displayBalance()
b1.deposit(2000)
b1.displayBalance()
b1.withdrawl(500)
b1.displayBalance()

class Employee:
    EmpName="Ram"
    EmpSalary=100000
    def __init__(self,location,role):
        self.location=location
        self.role=role
    def getInfo(self):
        print(self.EmpName,self.EmpSalary,self.location,self.role)
    @classmethod
    def update(cls,newSalary):
        cls.EmpSalary=newSalary
E1=Employee("Hyderabad","SDE")
E1.getInfo()
E1.update(1400000)
E1.getInfo()



        






 




   










