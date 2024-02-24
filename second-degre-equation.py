from math import sqrt
from fractions import Fraction

print("for solving this equation ax^2 + bx + c = 0 ")
a = float(Fraction(input("Enter the first number: ")))
b = float(Fraction(input("Enter the Second number: ")))
c = float(Fraction(input("Enter the last number: ")))

Delta = (b ** 2) - 4 * (a * c)

# D = 0
if Delta == 0 :
   X = -b / (2 * a)
   print("The Solution is : " , "X =",Fraction(X))

# D < 0 (Complex Solution)
if Delta < 0:
   A1 = (-b / (2 * a))
   B1 = ( sqrt(-Delta) / (2 * a))
   B2 = (-sqrt(-Delta) / (2 * a))
   
   Z1 = Fraction(A1) + Fraction(B1)*1j
   Z2 = Fraction(A1) + Fraction(B2)*1j

   print("The Solution is: Z1 = ", Z1 ,"and Z2 = ", Z2)

# D > 0
if Delta > 0 :
   X1 = (-b + sqrt(Delta)) / (2 * a)
   X2 = (-b - sqrt(Delta)) / (2 * a)
   print("The Solution is : " , "X1 =", Fraction(X1) ,"and", "X2 =", Fraction(X2))
