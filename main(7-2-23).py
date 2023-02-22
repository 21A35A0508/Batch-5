#while loop
# n=int(input("enter n value:"))
# i=0
# while(i<=n):
#     if(n%2==0):
#         print(i,end=" ")# produces space back to back
# i=i+1

#calculate sum of numbers:
# num=int(input("enter a natural number:"))
# if(num<0):
#     print("please enter a positive number")
# else:
#     sum = 0
#     while(num%2==0):
#       sum=sum+num
#       num=num-1
# print("sum is:",sum)

# #fibonacci series
# nterm=int(input("enter the no.of terms:"))
# n1=0
# n2=1
# count=0
# if(nterm<=0):
#     print("enter a valid input")
# elif(nterm==1):
#     print(n1)
# else:
#     while(count<nterm):
#         print(n1)
#         nt=n1+n2
#         n1=n2
#         n2=nt
#         count+=1


#
#
# #program to add all the digits in a number
# num=int(input("enter a number:"))
# sum=0
# while(num!=0):
#     r = num % 10
#     sum=sum+r
#     num = num // 10
# print("sum=",sum)
#  #125=1+2+5=8

#calculate even and odd numbers separately
# num=int(input("enter a natural number:"))
# i=o=e=0
# while(i<=num):
#     if num%2==0:
#         e=e+i
#     else:
#         o=o+i
#         i=i+1
# print("even sum:",e)
# print("odd sum:",o)

# if(num<0):
#     print("please enter a positive number")
# else:
#     sum = 0
# while(num>0):
#     if(num%2==0):
#         sum=sum+num
#         num=num-1
#         print("sum is:",sum)
#     elif(num%2!=0):
#         sum=sum
#         print("")
#
#
# num=int(input("enter a natural number:"))
# if(num<0):
#     print("please enter a positive number")
# else:
#     sum = 0
# while(num>0):
#     if(num%2==0):
#         sum=sum+num
#         num=num-1
# print("sum:",sum)

#reverse a number
# n=123
# while(n>0):
#     temp=n%10
#     print(temp,end="")
#     n=n//10

#binary to decimal conversion
# d=int(input("enter a number:"))
# b=i=0
# while(d!=0):
#     r=d%2
#     b=b+r*(10**i)
#     d=d//2
#     i=i+1
# print(b)

#binary to decimal
# binary = int(input('Enter a Binary number: '))
# deci=0
# p=0
# while binary>0:
#     q=binary//10
#     r=binary%10
#     deci = deci + r*2**p
#     p +=1
#     binary=q
# print(" Decimal is ", deci)

# for i in range(0,14,3):
#     print(i)

    # program to calculate total of n natural no's and find average--n=10
# n=10
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
#     avg=sum/n
# print(i)
# print("sum=",sum)
# print("average=",avg)

#print multiplication table
# n=int(input("enter a number:"))
# for i in range(0,21):
#     print(n,"*",i,"=",n*i)

#program to calculate factorial of given number
# n=int(input("enter number:"))
# fact=1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

#1+1/2+1/3+1/4---1/n  n=10
# s=0.0
# n=int(input())
# for i in range (1,n+1):
#     a=1.0/i
#     s=s+a
# print(s)

#1/2+2/3+3/4+-----n/n+1
# s=0.0
# n=int(input())
# for i in range (1,n+1):
#     a=i/i+1
#     s=s+a
# print(s)

#find difference of even and odd index sum(1227-->1+7  2+2=8-4=4
# n=int(input())
# e=0
# o=0
# for i in n:
#     if(n%2==0):
#         e=e+int(i)
#     else:
#         o=o+int(i)
# print(round(o-e))


#TCS question max of 4 digit to base17 as i/p and o/p its decimal value
# n=str(input())
# t=''
# for i in n:
#     if i in "ABCDEFGabcdefg":
#         t=int(n,17)
#     else:
#         print(t)
# print(int(n,17))

                    #or
# n=str(input())
# t=int(n,17)
# print(t)

# ab=[1,2,34,5,43]
# for i in ab:
#     if(i==34):
#         continue      # same break
#     print(i)

# for letter in'Pavani':
#     pass
#     print(letter)

    #calendar program
# import calendar
# y=2022
# m=5
# cal=(calendar.month(y,m))
# print(cal)
                             #or
# import calendar
# y=int(input("enter year:"))
# cal=calendar.TextCalendar(calendar.SUNDAY)
# i=1
# while i<=12:
#     cal.prmonth(y,i)
#     i+=12