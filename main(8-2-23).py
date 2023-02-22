#string basic format
# txt='pavani'
# index=0
# for i in txt:
#     print("message[",index,"]=",i)
#     index+=1

#string function zerofill--zfill
# n="hello world"
# print(n.title())  #or capitalise
# n=8
# print(n.zfill(5))

# y="pavani"
# print(y[1:5])   #avan
# print(y[0:5])   #pavan
# print(y[0:7])  #pavani
# print(y[:])  #pavani
# print(y[-3])  #a
# print(y[::-1])  #reverse of string  #inavap
# txt="india is mu country"
# print(txt[::2])

# ch=" "
# print(ord(ch))    #32
# print(chr(97))    #0(ascii value)

# txt1='india is great'
# txt2=' i'
# if txt2 in txt1:
#     print("found")
# else:
#     print("not found")

# txt1='india is great'
# for i in txt1:
#     print(i,end=" ")

# txt='india is a country'
# i=0
# while i<len(txt):
#     l=txt[i]
#     print(l,end=" ")
#     i=i+1

#pattern
# n=int(input())
# for i in range(1,n+1):
#      ch='A'
#      print()
#      for i in range (1,i+1):
#          print(ch,end=" ")
#          ch=chr(ord(ch)+1)

# txt='india is a country'
# i=0
# while i<len(txt):
#     l=txt[i]
#     print(chr(ord(l)+2),end=" ")
#     i=i+1

#program that accepts a string from user and redisplays the same string after removing vowels from it
string=input("enter a string:")
vowels=['a','e','i','o','u']
result=""
for i in range(len(string)):
    if string[i] not in vowels:
        result=result+string[i]
print(result)

# l=[1,2,3,4,5,6,7,8,9,10]
# print(l[3])
# print(l[2:5])
# print(l[::2])
# print(l[1::3])
# print(list.append(11))
# print(l)