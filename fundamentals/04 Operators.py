'''
Python Operators
Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators


# Arithmetic operators 
  + - * / % 
  **  Exponentiation 
  //  Floor division

# Assignment operators
=	x = 5	x = 5
+=	x += 5	x = x + 5
-=	x -= 5	x = x - 5
*=	x *= 5	x = x * 5

# Comparison operators
>	Greater that - True if left operand is greater than the right,	x > y
<	Less that - True if left operand is less than the right,	x < y
==	Equal to - True if both operands are equal,	x == y
!=	Not equal to - True if operands are not equal,	x != y
>=	Greater than or equal to - True if left operand is greater than or equal to the right,	x >= y
<=	Less than or equal to - True if left operand is less than or equal to the right,	x <= y

# Logical operators
and	True if both the operands are true,	x and y
or	True if either of the operands is true,	x or y
not	True if operand is false (complements the operand),	not x


# Identity operators
is	True if the operands are identical (refer to the same object)	x is True
is not	True if the operands are not identical (do not refer to the same object)	x is not True

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)


# Membership operators
in	True if value/variable is found in the sequence	5 in x
not in	True if value/variable is not found in the sequence	5 not in x

x = 'Hello world'

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Bitwise operators
&	Bitwise AND	x& y = 0 (0000 0000)
|	Bitwise OR	x | y = 14 (0000 1110)
~	Bitwise NOT	~x = -11 (1111 0101)
^	Bitwise XOR	x ^ y = 14 (0000 1110)
>>	Bitwise right shift	x>> 2 = 2 (0000 0010)
<<	Bitwise left shift	x<< 2 = 40 (0010 1000)
'''