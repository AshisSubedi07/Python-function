#main focus on indentation:
#Function for single operation AM mean 
def Ammean(a,b):
    mean=(a+b)/2
    print(mean)
a=int (input("Enter the value of a: "))
b=int (input("Enter the value of b: "))

print("The Arithmetic mean of",a, "and",b, "is: ")
Ammean(a,b)

#Single use of function greater for conditional statements of arguments of function Ammean
def greater(a,b):
    if (a>b):
        print("A is greater than B")
    elif (a==b):
        print("Both the numbers are equal")
    else:
        print("B is greater than A")

greater(a,b)

#using same function for two operations i.e the multiplication and division.
def operation(i,j):
    mul=i*j
    print(mul)
i=int(input("Enter the value of i: "))
j=int(input("Enter the value of j: "))
print("The multiplication of" ,i, "and" ,j, "is: ")
operation(i,j)

def operation(l,m): #same function name i.e operation
    div=l/m
    print(div)
l=int(input("Enter the value of l: "))
m=int(input("Enter the value of m: "))

print("The division of",l,"and",m,"is; ")
operation(l,m)

