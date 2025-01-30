import decimal

from decimal import Decimal



# Set precision to 50 decimal places

decimal.getcontext().prec = 100



a = Decimal('22140420794752410611752666524851109888000000000000000000000000')

b = Decimal('7047514823238872026048479698811123114346110918644208851504446')

c = 360


print(f"multiplier:{c}")
print(a*c)

print(b*c)