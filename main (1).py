print("Hello, World!")

print(23)

print(2+4)

#variables

name = "nida"
age = 18 
marks = 99.9

print(name)
print(age)
print(marks)

print("my name is nida:")
print("my age is 18:")



print("my name is :",name)
print("my age is :",age)
print("my marks is :",marks)

age2 = age 

print(age2)

#data type 
    # int / float / str

print(str("nida"))
print(int(24))
print(float(45))

# type
print(type(23))
print(type(2.3))
print(type("23"))

#boolean / none 

age = 18
old = False
a = None

print(type(old))
print(type(a))

#keywords 
   #True 
   #False
   #None
   
   #print sum

a = 5
b = 8
sum = a + b 
print(sum)

#print diff

a = 8
b = 4
diff = a + b 

print(diff)

#comment in py.
      # single line comment
      # single line comment
      # single line comment
    #multi line comment

print("hello world") # hello world
#print("hello world")

#type of operators 
 
 #arithmetic operator
  
a = 5
b = 2

total = a + b 

print(total)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b) #5^2
print(a % b) #reminder 

#relation / comparison operators 
      # True
      # False
      
a = 60
b = 50

print(a == b) 
print(a <= b)
print(a >= b)
print(a != b)

#assignment operators 

num = 10
num = num + 10 # 20
print(num)

# num +=10 

num = 10 
num += 10 
print("num :", num)

num *= 10 
print("num :", num)

num /= 10
print(" num :", num)

num **= 10 
print("num :", num)

num %= 10 
print("num:", num)

#logical operators (not, and , or)

               # and

val1 = False
val2 = True
 
print("and operators :",val1 and val2 )

                  #or

print("or operators :" , val1 or val2)

                  #not

print(not False)
print(not True)

a = 20
b = 30 

print("or operators :",(a <= b))
print("or operators:", (a >= b))
print("or operators:", (a == b))

print("or operators:",(a <= b) or (a < b))
print("and operators:",(a == b) and (a >= b))
print("and operators:",(a <=b) and (a < b))


#type conversion 
 
a = 2
b = 4.5
c = "2"

sum = a + b

print(sum)

print(type(a)) # int
print(type(b)) # float 
print(type(c)) # str

#type costing 

a = int("2")
b = 2.5
print(type(a)) # int
print(type(b)) # float

a = float("2")
b = 2.4
print(type(a))

a = 3.45
a = str(a)
print(a) 

#input in py.

name = input("enter your name:")
print("welcome",name)

val = int(input("enter some value :"))
print(type(val),val)

name = input("enter name")
age = input(" enter age")
marks = input(" enter marks")

print("name :", name)
print("age =", age)
print("marks =", marks)


      #let'practice 
      
#write a program to input 2 number and print thier sum
#solve

first = int(input("enter first :"))
second = int(input("enter second :"))

print("sum=",first + second)

#2.WAP to input side of a square and print is  area

side = int(input("side of square:"))

print("area=",side * side )

#3.WAP to input 2 floating number and print thier average 

a = float(input("enter first"))
b = float(input("enter second"))

print("avg=", (a + b) /2)

 #4.WAP to input 2 int number ,a and b print true if a is grater than or equal to b if not print false 
 
a = int(input("enter first :"))
b = int(input("enter second :"))

print(a == b)
print(a >= b) 













