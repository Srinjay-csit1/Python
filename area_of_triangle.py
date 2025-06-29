a=int(input("Length of 1st arm="))
b=int(input("Length of 2nd arm="))
c=int(input("Length of 3rd arm="))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the triangle=",area)
