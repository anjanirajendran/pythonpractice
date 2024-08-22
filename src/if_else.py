# a == b, a !=b, a <b, a>b, a<=b, a>=b
a = 55
b = 70

if a == b:
    print("A is equal to b")
elif a > b:
    print("a is grater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is not equal to b")


if(a<b):
    if a < 33:
        print("a is less than 33")
    else:
        print("a is greater than 33 and less than b")
    print("a is less than b")

# Short hand notation of if else statements
print("------------------------------")
print("a is less than b") if a < b else print("a is greater than b")
print("======================================")

# short hand if statement
a = 60
b = 40
if a > b: print("a is greater than b")

# how to check mutliple condition in one sattement
# a, b and c a>b & b>c then I say a is the biggest number

a = 12
b = 10
c = 8
if a > b and b > c : print("a is the biggest number")