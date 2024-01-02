'''
FATHER:Guido van Rossum
released year:1991.
DEFINITION:python is high level interpreted object orienter programming language.
Tokens:
1.Identifiers
2.Keywords
3.Operators
4.Delimeter
5.Literals '''

#I a single line comment
'''multiline comment'''

#basic of pythons
print("1.THE BASICS OF PYTHON:")#using print function.
get=input("WHAT PROGRAMS YOU GOING TO EXECUTE ?\n")#using input function
'''
1.Identifiers
get
(it is just name given to that value.its our wish to name a value but it has some condition)
is a identifier which store value and use for future
*Identifiers cannot be a keyword.
*Identifiers are case-sensitive.
*It can have a sequence of letters and digit but the first letter of an identifier cannot be a digit.
*Whitespaces are not allowed.
*We cannot use special symbols like !, @, #, $, and so on.
'''

'''
function is set of code it will execute when we call
types:
*built in function:It is already defined we just call its name and use in our program for.
for example add() is bulit in function,add(1,2) returns output 3.
*user defined function:refer below
'''


print("2.keywords in python")
'''2.keywords are reserved words that do specific function'''
import keyword
print(keyword.kwlist)


print('3.Different data types:')

a=1
print(a)
print(type(a))#type() is built in function it return data type
b=1.1
print(b)
print(type(b))
c='python'
print(c)
print(type(c))
bol=True
print(bol)
print(type(bol))
d=[1,2,3,4,5]
print(d)
print(type(d))
dic={"key":6,"brand":"apple"}
print(dic)
print(type(dic))
list1=[1,2,3,4,5]
print(list1)
print(type(list1))
set1={1,2,3,4,5}
print(set1)
print(type(set1))
list2=(1,"python",4.5,2,3,4,5)
print(type(list2))
print("------------------------------------------------------------------------------------------------------")
print()
#simple math operation
a=int(input("enter values:"))#getting value from
b=int(input("enter values:"))
print("ADDITION OF GIVEN NUMBERS IS ",a+b)#a+b print value of a+b.#python is case sensitive
print()#used for line spacing purpose in output screen ''not manditory''  
print("------------------------------------------------------------------------------------------------------")#used to indicate end of program
print()
print("4.operators")
def ari_operator(a,b):
          print("The arithmetic operators are:")
          print("a+b=",a+b)
          print("a-b=",a-b)
          print("a/b=",a/b)
          print("a*b=",a*b)
          print("a//b=",a//b)
          print("a%b=",a%b)
          print("a**b=",a**b)


ari_operator(3,2)

print()
print("------------------------------------------------------------------------------------------------------")
print()
def assign_operator(a,b):
          print("The sssignment operators are:")
          a=5
          b=6
          print("a=",a)
          print("b=",b)
          a+=b
          print("a+=b=",+b)
          a-=b
          print("a-=b=",a)
          a*=b
          print("a*=b=",a)
          a//=b
          print("a//=b=",a)
          a%=b
          print("a%=b=",a)
          a**=b
          print("a**b=",a)
          
assign_operator(3,4)
print()
print("------------------------------------------------------------------------------------------------------")
print()



def comparison_operator(a,b):
          print("The comparison oprator are:")
          print("a==b:",a==b)
          print("a!=b:",a!=b)
          print("a<b:",a<b)
          print("a>b:",a>b)
          print("a<=b:",a<=b)
          print("a>=b:",a>=b)

comparison_operator(4,2)
print()
print("------------------------------------------------------------------------------------------------------")
print()

def logical_operator():
          print("The logical oprator are:")
          if 5==5 and 4==4:
                    print ("I am logical 'AND' I will execute when both condition are true.")
          if (5<5) or (4==4):
                    print ("I am logical 'OR' I will execute when atleast one condion is true")
          '''val1=2
          val2=3
              print ("I am logical 'NOT' I will execute when condition results complement")'''

logical_operator()

print()
print("------------------------------------------------------------------------------------------------------")
print()

def member_opeartor():
           print("The membership oprator are:")
           str="python"
           print('p' in str)
           print('p' not in str)


member_opeartor()

print("------------------------------------------------------------------------------------------------------")
def identy_operator():
          print("The identity oprator are:")
          str="python"
          print(str[0] is str[1])
          print(str[0] is not str[1])


identy_operator()

print()
print("------------------------------------------------------------------------------------------------------")
print()

#condition statement
a,b,c=6,6,7
print("5.Condition statements")
print("THE CONDITION STATEMENT IN PYTHON ARE:")

print("I.odd or even using if else statement")

e_o=int(input("enter value to check odd or even:"))

if (e_o%2==0):
          print("given number is even")
else:
          print("given number is odd")

print()
print("------------------------------------------------------------------------------------------------------")
print()


print("II.greatest of three number using if else statement")
if (a>b) and (a>c):
          print("a is greater")
elif(b>c):
          print("b is greater")
else:
           print("c is greater")


print()
print("------------------------------------------------------------------------------------------------------")
print()




print("III.voting eligibility using if else statement")
age=int(input("enter age:"))
if age>18:
          print("you are eligible to vote")
elif age==18:
           print("apply voter id")
else:
           print("you are not eligible to vote")


print()
print("------------------------------------------------------------------------------------------------------")
print()


#LOOPING STATEMENT ARE:
print("6.Looping statements")
print("THE SIMPLE LOOPING STATEMENT")
print("using for:")
print("I.First 5 natural numbers")
for i in range(1,6):
          print(i)

print()
print("------------------------------------------------------------------------------------------------------")
print()


print("II.First 5 even numbers")
for i in range(0,10,2):
          print(i)

print()
print("------------------------------------------------------------------------------------------------------")
print()


print("III.First 5 odd numbers")
for i in range(1,10,2):
          print(i)

print()
print("------------------------------------------------------------------------------------------------------")
print()


print("using while:")
print("I.First 5 natural numbers")
i=1
while(i<6):
      print(i)
      i=i+1

print()
print("------------------------------------------------------------------------------------------------------")
print()


i=0
print("II.First 5 even numbers")
while(i<10):
      print(i)
      i=i+2

print()
print("------------------------------------------------------------------------------------------------------")
print()


print("III.First 5 odd numbers")
i=1
while(i<10):
      print(i)
      i=i+2

print()
print("------------------------------------------------------------------------------------------------------")
print()
      













           
           
           




        

          
              
          

