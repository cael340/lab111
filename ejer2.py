import math
a=input("introducir valor de a: ")

b=input("introducir valor de b: ")

c=input("introducir valor de c: ")

X1= (int(b^2 + (math.sqrt(b^2+4*a*b))/2*a))
X2= (int(b^2 - (math.sqrt(b^2+4*a*b))/2*a))

print("la ecuacion cuadratica 1 es: ", X1)

print("la ecuacion cuadratica 2 es: ", X2)
