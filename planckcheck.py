import decimal
from decimal import Decimal

# Set precision to 50 decimal places
decimal.getcontext().prec = 100

numerator = Decimal('7970551486110867820230959948946399559680000000000000000000000000')
denominator = Decimal('2537105336365993929377452691572004321164599930711915186541600717')

# More precise value of pi (50 decimal places)
actual_pi = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')

approximation = numerator / denominator
print(f"{numerator}")
print(f"{denominator}")
print(f"Approximation: {approximation}")
print(f"Actual π:      {actual_pi}")
print(f"Difference:    {abs(approximation - actual_pi)}")

# Calculate correct digits
correct_digits = 0
for digit1, digit2 in zip(str(approximation), str(actual_pi)):
    if digit1 == digit2:
        correct_digits += 1
    else:
        break

print(f"\nCorrect digits: {correct_digits - 2}")  # Subtract 2 for the "3." at the start

# Calculate at cosmic scale
planck_length = Decimal('1.616255E-35')  # meters
universe_diameter = Decimal('8.8E26')  # meters

pi_cosmic_error = abs(approximation - actual_pi) * universe_diameter / planck_length

print(f"\nError at universe scale in Planck lengths: {pi_cosmic_error}")
print(f"Error at universe scale in meters: {pi_cosmic_error * planck_length}")