# Iterating through digits in a number

If you want to iterate through a number of digits say 12345, you might think to first convert the number to a string, iterate through each character, and then convert each character back to an integer.

## Key Idea

To access each digit in a number, you can use the modulus(`%`) and integer division (`//`) operations. The modulus operation gives you the last digit of the number, and integer division removes that last digit.

## Steps

1. Get the last digit: Use the modulus operation (`% 10`) to extract the last digit of the number.
2. Remove the last digit: Use integer division (`// 10`) to remove the last digit from the number.
3. Repeat: Continue this process until all digits have been processed.

## Example

```py
# Example: Finding the sum of digits in a given number
num = 12345
sum_num = 0

while num > 0:
    digit = num % 10  # Isolates the last digit (5, then 4, then 3, etc.)
    sum_num += digit  # Adds the digit to the sum
    num //= 10  # Removes the last digit from the number (1234, then 123, etc.)

print(sum_num)  # Output will be 15 (1 + 2 + 3 + 4 + 5)
```
