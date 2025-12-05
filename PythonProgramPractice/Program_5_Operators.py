'''
python operators = arithmatic operators,relational operators,assignment operators,logical operators,other operators
Arithmatic operators = addition(+),subtraction(-),multiplication(*),division(/),modulos(%),floor division(//),exponential(**)
relational operators = < , > , <= , >= , ==, !=
assignment operators = =, +=, -=, *= , /= , %= , //= etc.
logical operators = and, or, not
other operators =  identity operator, bitwise operator, membership operator

Operator precedence
() = highest priority
** = second priority
*,/,//,% = third priority same priority (execution starts from left to right)
+ , - = fourth priority same priority (execution starts from left to right)

'''
a, b = 10, 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print(True and True)
print(True or False)
print(not True)
print(not False)
print(False or False)
