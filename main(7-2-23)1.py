#sum of n natural numbers

num=int(input("enter a natural number:"))
if(num<0):
    print("please enter a positive number")
else:
    sum = 0
while(num>0):
    sum=sum+num
    num=num-1
print("sum is:",sum)


#while loop
# n=int(input("enter n value:"))
# i=0
# while(i<=n):
#     print(i,end=" ") # produces space back to back
#     i=i+1
