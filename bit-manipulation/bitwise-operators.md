# Bitwise Operators

Bitwise operators work on a single bit of data, which is the smallest unit of data a computer can process and store (has a value of either 0 or 1).

The smallest unit of addressable space(space that can be referenced) that CPUs use to store data is a ***byte***, which is made up of 8 bits, making it the smallest unit of space a variable can reference.
For example, a boolean value like True, which should really take one bit as it evaluates to 1, will be stored as one byte: `00000001`.

## Why bitwise operators are used
- Useful for writing algorithms for encryption and video compression
- Useful for performing operations in embedded devices that have memory limitation


## Operators

### AND Operator
The `AND` operator, usually symbolized by `&` in most programming languages does a bit by bit comparison of each number. Given two numbers, the `&` operator compares the numbers bit by bit, and if both bits are 1, it returns `1`, otherwise, `0`. For example the operation `6 & 7` will first convert the two numbers to binary: `110 & 111` and then return `110` and converted as `6` since `1&1 = 1`, and `1&0 = 0`

In a unix file system, the `&` operator can be used as a test to see if a user has the needed permission by comparing their permissions permissions against their required permission to see if there's a match.
E.g: given file system permissions: read(r), write(w) and execute(x), if an operation requires read and write rights, but not execute right, the operations permission can be represented as `110` (which is 6), 1 for r, 1 for w and 0 for x. If a user has this permission `100`(which is 4), then the user can only read, but not write or execute. To check if the user has the required rights, we can use the operation `4&6` to check for the intersection of the user's rights and the required rights. This will evaluate to 4 (`110`) confirming that the user indeed has the read right required by the operation.

### OR Operator
The `OR` operator, represented as `|` compares each individual bit and returns `1` if any of the bits are set to `1`. E.g. `1|0 = 1` and `0|0 = 0`.
In the file system example, the `|` operator can be used to remo