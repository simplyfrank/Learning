from decimal import Decimal

from fractions import Fraction
two_thirds = Fraction(2,3)
four_fifth = Fraction(4,5)

# 
Fraction(3094580234985034985304958234059834059)

Fraction(Decimal('0.1'))

# Arithmetic with Fractions
Fraction(2,3) + Fraction(4,5)
Fraction(2,3) - Fraction(4,5)
Fraction(2,3) * Fraction(4,5)
Fraction(2,3) / Fraction(4,5)
Fraction(2,3) // Fraction(4,5)
Fraction(2,3) % Fraction(4,5)

# Construct Fractions from strings
Fraction('2', '4')

# Fraction Type does not support standard math functions
from math import floor
floor(Fraction('4/3'))