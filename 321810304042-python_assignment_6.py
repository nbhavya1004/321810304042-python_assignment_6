# 321810304042-python_assignment_6

# Bhavyasree N - 321810304042

#    1.    Generate first N number of Fibonacci numbers. Take N value from user.

# METHOD_1 :

def Fibonacci(num) :
	num1 = 0
	num2 = 1
	series = 0
	for i in range(num) :
		print(series,end=' ')
		num1 = num2
		num2 = series
		series = num1 + num2
num = int(input('Enter the number of items in Fibonacci series :'))
Fibonacci(num)

# METHOD_2 :

num = int(input("Enter number of digits(minimum 2) : "))
first = 0
second = 1
print("Fibonacci series is : ")
print(first, "," , second, end = ",")
for i in range(2,num) :
	next = first + second
	print(next , end = " , ")
	first = second
	second = next

# METHOD_3 :

n=int(input("enter the number"))
a=0
b=1
count=0
if n<0:
	print("enter the positive number")
elif n==1:
	print("fibonacci series upto ",n)
	print(a)
else:
	print("fibonacci series are:")
	while count<n:
		print(a)
		sum=a+b
		a=b
		b=sum
		count=count+1
	

    	


#    2.    Display multiplication table of K. Take k value from user.for Ex: 7 x 1 =7 , 7 x 2 = 14 ..... 

# METHOD_1 :

def table(n) :
	 for i in range(1,11) :
	 	print("%d * %d = %d" %(n,i,n*i))
n = int(input('Enter the value of k : '))
table(n)

# METHOD_2 :

n=int(input("enter the number:"))
for i in range(1,11):
	print(n,  "x", i ,"=",n*i)





#     3.    Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers. 

# METHOD_1 :

x = int(input("Enter first number: "))  
y = int(input("Enter second number: "))  		
if x > y:  
       smaller = y  
else:  
       smaller = x  
for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
              hcf = i 
print("The HCF of",x,"and",y,"is",hcf)

# METHOD_2 :

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number :"))
gcd = 1
for i in range(min(num1,num2),0,-1) :
	if (num1 % i) == 0 and (num2 % i) == 0 :
		gcd = i
		break
print("The GCD of the two numbers is : ",gcd)





#     4.    Write a Python program to count the number of even and odd numbers from a series of numbers. 

list1 = [21,3,4,6,33,2,3,1,3,76]
even_count, odd_count = 0, 0
for num in list1:
   if num % 2 == 0:
      even_count += 1
   else:
      odd_count += 1
print("Even numbers available in the list: ", even_count)
print("Odd numbers available in the list: ", odd_count)





#      5.    Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x)