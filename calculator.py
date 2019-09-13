x = float(input('Enter your first number: '))
y = float(input('Enter your second number: '))
z = input('Enter an operator(+,-,/,*) =')
if z == '+':
 print(x+y)
elif z == '-':
 print(x-y)
elif z == '*':
 print(x*y)
elif y != '0' and z == '/':
 print(x/y)
elif y == '0':
 print("ZeroDivisionError")
