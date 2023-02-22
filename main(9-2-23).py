#abcederian series
# str1='ABCBEFG'
# str2="ate"
# for l in str1:
#     print((l+str2),end=" ")

# write a program to evaluate list of a cubes till ramge of 10
# cube=[]
# for i in range(11):
#     cube.append(i**3)
# print(cube)

#find sum and mean of series 0 to 10
# sum=0
# abc=[1,2,3,4,5,6,7,8,9,10]
# for i in range(11):
#     sum=sum+i
#     mean=(sum/len(abc))
# print(sum)
# print(mean)

# len()
# repetition()
# in
# not in
# max
# min
# sum
# a=[44,1,2,3,1]
# a.remove(44)
# print(a)
# print(a.append(111),a)
# print(sum(a))
# print(sorted(a))
# print(a.count(1))
# a.insert(0,0)
# all
# any
# list
# sorted
#reverse

#push
#pop
#peek
#peep operations

# tower of hanoi(4 disks)
# def hanoi(n,a,b,c):
#     if n>0:
#         hanoi(n-1,a,b,c)
#         if a:
#             c.append(a.pop())
#             hanoi(n-1,b,a,c)
# a=[1,2,3,4]
# b=[]
# c=[]
# hanoi(len(a),a,b,c)
# print(a,b,c)

# num=['A','1','abc','b','2']  #ascii based
# num.sort()
# print(num)

# txt=['p','a','v','a','n','i']
# txt[2:5]=[]
# print(txt)


#program to combine list of cubes given number
# cube=[i**3 for i in range(11)];print(cube)   #semi colon is used for connecting statements

# l=[1,2,3,4]
# for i in range(len(l)):
#     print("index of",i,":",l[i])

# l=[1,2,3,4,5,6,7,8]
# it=iter(l)
# for i in range(len(l)):
#     print("element index:",i,":",next(it))

# n= 10
# k = int(input())
# if k in range(1, 6):
# 	print('No. of Candies Sold:',k)
# 	print('No. of Candies Left:',n-k)
# else:
# 	print("Invalid Input")
# 	print('No. of Candies Left:',n)

# n=int(input("enter load:"))
# if n==0:
#     print("invalid")
# elif(n>0 and n<=2000):                     #elif n in range(1,2001)
#     print("estimated time is 25 min")
# elif(n>2000 and n<=4000):
#     print("estimated time is 35 min")
# elif(n>4000 and n<=7000):
#     print("estimated time is:45min")
# else:
#     print("overload")

# l=(7,6)
# for i in range(8):
#     n1=print(i*l[0])
# print(n1)
# for i in range(8):
#     n2=print(i*l[1]-1)
# print(n2)
# print()

#series--0,0,7,6,14,12,21,18---(interview)
# val=int(input("enter a value:"))
# n2=0
# for i in range(1,val+1):
#     if (i%2==0):
#         n1=n1+7
# else:
#     n2=n2+6
# if(val%2!=0):
#     print(format(val,val-7))
# else:
#     print(format(val,val-6))

                                   #or
a=7
b=6
i=j=temp=1
list=[]
n=int(input("enter n:"))
while(temp<=n):
    if temp%2!=0:
        list.append(a*[i-1])
        i+=1
    else:
        list.append(b*[j-1])
        j+=1
temp+=1
print("the {} term is {} ".format(n,list[n]))


# digital machine m 0's and 1's

