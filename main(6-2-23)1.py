# print('pavani' +'3')

# a=2
# b=4
# c=6
# s=a+b+c/2
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print(type(area))
# print(area)

# r=6
# print("circumference=:",2*3.14159*r)
# print("area=:",3.14159*pow(r,2))

# a=int(input())
# if a%2==0:
#     print("even")
# print("a is even")
# else:
#     print("odd")

# a=int(input("enter a number"))
# if(a>0):
#     print("positive")
# elif(a<0):
#       print("negative")
# else:
#     print("zero")

# a=int(input("enter a number:"))
# if a>0 and a<10:
#     print("range is 0 to 10")
# if a>=10 and a<20:
#     print("range is 10 to 20")
# if a>=20 and a<30:
#     print("range is 20 to 30")

# a=int(input("enter a value:"))
# b=int(input("enter b value:"))
# c=int(input("enter c value:"))
# if(a>=b):
#     if(a>=c):
#         print("a is largest")
#     else:
#         print("c is largest")
#
# else:
#   if(b>=c):
#       print("b is large")
#   else:
#       print("c is large")



# a=int(input("enter a value:"))
# b=int(input("enter b value:"))
# c=int(input("enter c value:"))
# if(a>=b) and (a>=c):
#     print("a is large")
# if(b>=c) and (b>=a):
#     print("b is large")
# else:
#     print("c is large")
#
# k=5
# n=int(input("enter value:"))
# if(k<=n):
#     print("invalid")
# if(n==0) or (k<n):
#     print("no.of candies sold:",k)
#     print("candies available:", n-k)
# if(n==k):
#     print("candies available:",k)


n= 10
k = int(input())
if k in range(1, 6):
	print('No. of Candies Sold:',k)
	print('No. of Candies Left:',n-k)
else:
	print("Invalid Input")
	print('No. of Candies Left:',n)

