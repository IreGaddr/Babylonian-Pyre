import decimal

from decimal import Decimal



# Set precision to 50 decimal places

decimal.getcontext().prec = 100



numerator = Decimal('7970551486110867820230959948946399559680000000000000000000000000')

denominator = Decimal('2537105336365993929377452691572004321164599930711915186541600560')



# More precise value of pi (50 decimal places)

actual_pi = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')



current_approximation = numerator / denominator


print(f"{numerator}")
print(f"{denominator}")
print(f"Current approximation: {current_approximation}")

print(f"Actual π: {actual_pi}")

print(f"Difference: {abs(current_approximation - actual_pi)}")



# Fine-tuning loop

best_denominator = denominator

best_difference = abs(current_approximation - actual_pi)



for i in range(-10000000, 10000001):

    test_denominator = denominator + i

    test_approximation = numerator / test_denominator

    difference = abs(test_approximation - actual_pi)

    

    if difference < best_difference:

        best_denominator = test_denominator

        best_difference = difference



best_approximation = numerator / best_denominator



print(f"\nBest denominator: {best_denominator}")

print(f"Best approximation: {best_approximation}")

print(f"Actual pi: {actual_pi}")

print(f"Improved difference: {best_difference}")



# Calculate correct digits

correct_digits = 0

for digit1, digit2 in zip(str(best_approximation), str(actual_pi)):

    if digit1 == digit2:

        correct_digits += 1

    else:

        break



print(f"\nCorrect digits: {correct_digits - 2}")  # Subtract 2 for the "3." at the start