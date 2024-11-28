# Bitwise Operators

Bitwise operators work on a single bit of data, which is the smallest unit of data a computer can process and store (has a value of either 0 or 1).

The smallest unit of addressable space(space that can be referenced) that modern CPUs use to store data is a ***byte***, which is made up of 8 bits.
For example, a boolean value like True, which should really take one bit as it evaluates to 1, will be stored as one byte: `00000001`.

## Why bitwise operators are used
- **Efficient Algorithms**: Used in encryption, video compression, and checksum calculations.
- **Low-level Programming**: Essential in embedded systems and devices with memory limitations.
- **Permission Systems**: Useful for managing and testing permission levels in file systems.


## Operators

### 1. AND(`&`) Operator
The `AND` operator, usually symbolized by `&` in most programming languages does a bit by bit comparison of each number. Given two numbers the `&` operator compares the numbers bit by bit:
- If both bits are 1, the result is 1.
- Otherwise, the result is 0.

For example the operation `6 & 7`, the operation will work as follows:
1. Convert numbers to binary:
    - `6 → 110`
    - `7 → 111`
2. Align the bits and perform the operation
    | 6  | 7  | 6 & 7 |
    | ---|--- | ----- |
    | 1  | 1  |   1   |
    | 1  | 1  |   1   |
    | 0  | 1  |   0   |

3. Convert back to decimal: `110 → 6`.

#### **Practical Use Case: File Permissions**
In Unix-like systems, file permissions are represented in bits:

- `r` (read) = `4` (`100`)
- `w` (write) = `2` (`010`)
- `x` (execute) = `1` (`001`)

To check if a user with `4` (read) has the necessary permission for an operation requiring `6` (read + write):

```py
    User's Permission:  100
    Required Permission: 110
                        ----
    Intersection (&):    100  (Result: 4)
```



### 2. **OR (`|`) Operator**
The `OR` operator compares each bit of two numbers:
- If either bit is `1`, the result is `1`.  
- Otherwise, the result is `0`.

| Input A | Input B | A \| B |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 1      |

#### Example: `4 | 2`
1. Convert numbers to binary:
   - `4 → 100`  
   - `2 → 010`
2. Align the bits:
    ```py
        100  
        010  
        ----
        110  (Result in binary)
    ```
3. Convert back to decimal: `110 → 6`.

#### **Practical Use Case: Combine Permissions**
Suppose a user has `4` (read) and `2` (write) permissions but needs combined read + write permissions:
```py
Read (4):  100
Write (2): 010
           ----
Combined:   110  (Result: 6, Read + Write)

```


---

### 3. **NOT (`~`) Operator**
The `NOT` operator inverts all bits of a number:
- `1` becomes `0`, and `0` becomes `1`.

#### Example: `~5`
1. Binary for `5` (in 8 bits): `00000101`.  
2. Invert all bits: `11111010`.  
3. Convert back to decimal: `-6` (which is the complement of 5).


### 4. **XOR (`^`) Operator**
The `XOR` operator compares each bit:
- If the bits are different, the result is `1`.  
- If the bits are the same, the result is `0`.

| Input A | Input B | A ^ B |
|---------|---------|-------|
| 0       | 0       | 0     |
| 0       | 1       | 1     |
| 1       | 0       | 1     |
| 1       | 1       | 0     |

#### Example: `5 ^ 3`
1. Binary for `5`: `101`.  
2. Binary for `3`: `011`.  
3. XOR the bits:
    ```py
    101  
    011  
    ----
    110  (Result: 6 in decimal)

    ```


### 5. **Shift Operators (`<<`, `>>`)**
Shift operators move the bits of a number left or right:
- **Left Shift (`<<`)**: Adds zeros to the right, effectively multiplying by `2^n`.  
- **Right Shift (`>>`)**: Removes bits from the right, effectively dividing by `2^n`.

Note: `n` is the number of positions by which a number is being shifted. So in `3 << 2`, `n` is `2`.

**This is the logic**: Take left shift:
- if you left shift a number by 1 place, you add 0 to the binary representation of the number, so you're effectively multiplying by 2, since binary operations are in base 2.

- If you left shift by 3, you're adding three 0s to the binary number, so you're multiplying it by 2 x 2 x2 which is 2^3. 

- This is the same logic when dealing with decimal numbers(numbers in base 10). 
- If you add a single 0 to a number like 6, you get 60, meaning you've multiplied it by 10. 
- If you add two 0s to get 600, you've multiplied it by 10^2 and so on.

Similar logic will apply to a right shift, just that this time around, we divide instead of multiplying.

#### Example: Left Shift `3 << 2`
1. Binary for `3`: `11`.  
2. Shift two places to the left: `1100`.  
3. Result: `12` in decimal.

#### Example: Right Shift `8 >> 1`
1. Binary for `8`: `1000`.  
2. Shift one place to the right: `0100`.  
3. Result: `4` in decimal.


## Applications Recap
1. **File Permissions**: Efficiently manage and check access rights.
2. **Encryption**: XOR is widely used in simple encryption algorithms.
3. **Graphics**: Manipulate color channels for image blending.
4. **Networking**: Calculate subnet masks and optimize routing.

