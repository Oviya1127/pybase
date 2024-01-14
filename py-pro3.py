#simple python programs
a="oviya" #compile time assingnment
b=a[::-1]
if a==b:
          print("given string ",a,"is palindrome")
else:
          print("given string",a,"is not palindrome")
print()
print("------------------------------------------------------------------------------------------------------")
print()
str1=input("please enter string to check palindrome:") #run time assingment
b=str1[::-1]
if str1==b:
          print("given string ",str1,"is palindrome")
else:
          print("given string ",str1,"is not palindrome")
print()
print("------------------------------------------------------------------------------------------------------")
print()
print("armstrong number program")
num=int(input("enter value to check armstrong:"))
temporary=num
i=0
arm=0
while(i<num):
          r=num%10
          arm=arm+(r**3)
          num=num//10
if temporary==arm:
          print("given number is armstong")
else:
          print("given number not is armstong")
print()
print("------------------------------------------------------------------------------------------------------")
print()
#largest number in list
list1=[2,3,4,5,6,7,8,9]
print(list1)
i=0
max=list1[i] #fixing value compare with other list element
for i in range(0,len(list1)):
          if max<list1[i]:
                    max=list1[i] #changing value when condition is true
print("the maximum value is",max)
print()
print("------------------------------------------------------------------------------------------------------")
print()
#smallest number in list
min=list1[i]
for i in range(0,len(list1)):
          if min>list1[i]:
                    min=list1[i]
print("the maximum value is",min)
print()
print("------------------------------------------------------------------------------------------------------")
print()
#factorial of given number
fact=1
num=int(input("enter value for factorial :"))
while(num>0):
          fact=fact*num
          num=num-1
print("The factorial of number is:",fact)
print()
print("------------------------------------------------------------------------------------------------------")
print()

#area of shapes
s=int(input("enter side of square :"))
l=int(input("enter length of rectangle :"))
b=int(input("enter breadth of rectangle :"))
r=int(input("enter radius of circle:"))
h=int(input("enter height of triangle:"))
def sqrt(a):
          area=a*a
          print("area of square is",area)
def rect(l,b):
          area=l*b
          print("area of rectangle is",area)
def circle(r):
          area=3.15*r*r
          print("area of circle is",area)
def tri(b,h):
          area=(1/2)*b*h
          print("area of triangle is",area)
sqrt(s)
rect(l,b)
circle(r)
tri(b,h)
print()
print("------------------------------------------------------------------------------------------------------")
print()
#length of array and string:
ar=[1,2,3,4,5,6]
print(" The length of given array is:",len(ar))
a="oviya"
print(" The length of given string is:",len(a))
print()
print("------------------------------------------------------------------------------------------------------")
print()
#manual
length=0
for i in ar:
          length=length+1
print(" The length of given array using loop:",length)
length=0
for i in a:
          length=length+1
print(" The length of given string using loop:",length)
print()
print("------------------------------------------------------------------------------------------------------")
print()

#prime or not
num=int(input("enter value to check prime or not:"))

if num==1:
    print("given number is neither composite nor prime")
elif num>1:
    for i in range(2,num):
          if(num%i)==0:
                    print("Given number is not prime")
                    break
    else:
        print("Given number is prime")
else:
    print("invalid input!")
          
print()
print("------------------------------------------------------------------------------------------------------")
print()

























          


          

          



