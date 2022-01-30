from cmath import sqrt

# Inputs
a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

# Conversions
a=float(a)
b=float(b)
c=float(c)

# Calculations
root1 = ((b*-1) + sqrt((b*b)-(4*a*c)))/(2*a)
root2 = ((b*-1) - sqrt((b*b)-(4*a*c)))/(2*a)

print(f"Root 1 is {root1}\nRoot 2 is {root2}")