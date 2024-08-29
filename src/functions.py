# function is block of code
def my_function():
    print("I'm inside the function")
    return True

#my_function()

def function_param(param):
    print("Welcome to ", param)


#function_param("Python Class")
#function_param("Learning on Python")

def print_name(first_name, last_name):
    print("Hi Welcome "+ first_name +" " + last_name)

#print_name("Anajani", "Rajendran")
#print_name("Supriya", "Bandaru")

#print_name("Anjani") # error needed two aruguments

def family(*args):
    print(args[1]+ " :Head ogf house")

#family("father", "motheer", "sister", "brother")

def my_function_test(sib1, sib2, sib3):
    print("These are my sibilings "+sib1+" "+sib2+" "+sib3)

#my_function_test(sib2="sai", sib1="surya", sib3="Anjani")

def my_country(country = "India"):
    print("I am from "+country)

#my_country("Sweden")
#my_country("USA")
#my_country()

colors = ["green", "blue", "red", "black", "orange"]

def color_coding(arg):
    for x in arg:
        print("Color is "+x)

#color_coding(colors)

# write a function that helps ypu to determone whether the number is EVn or Odd

def even_odd(num):
    result = 0
    if(num%2 == 0):
        result = num*3
        #print(str(num)+" is an Even number")
    else:
        result = num*2
        #print(str(num)+" is an odd number")
    return result

#2 --> 2*3 ==6
#3 --> 3*2 == 6
var1 = even_odd(3)
var2 = even_odd(10)
#even_odd(36438919623961340)
#even_odd(9382610215)

print("result = ",var1)
print("result = ",var2)

# Recursive function 
# factorail 3!= 3*2*1 , 5!= 5*4*3*2*1

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

#result = factorial(5)
#print("factorail value is ", result)

# let's say I am passing 5
#line 1- n: 5 --> 5 * 4 * 3 * 2 * 1 ==> fcat(5)
# line2 - n: 4 --> 4 * 3 * 2 * 1  ==> fact(4)
#line 3- n:3 --> 3 * 2 * 1 ==> fact(3)
#line4 - n: 2 --> 2 * 1) ==> fact(2)
#line5 - n:1 --> 1 ==> fact(1)

# fibonacci sequence
# 5 --> 0,1 -- 1 --> 1+1 ->2

# 0,1,1,2,3,5,8,13,21, ...

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        print(fibonacci(n-1) + fibonacci(n-2))
        print("------")
        return fibonacci(n-1) + fibonacci(n-2)

res = fibonacci(7)
print("Result =",res)