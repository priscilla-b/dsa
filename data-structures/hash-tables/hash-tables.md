# Hash Tables

The hash table data structure combines **hash functions** and **arrays**.

***A hash function*** is a function that takes a string as an input and returns a number.
Hash functions map strings to numbers.
Has the following requirements:

- needs to be consistent. same value should be returned for same input at all times
- every input should be mapped to a different output

When combined with arrays, the output of the hash function represents the index of the arrays. These indexes are then used as markers for the items stored in the arrays.
So basically, a hash function input maps to an index, and then the index is the storage location of a value.
This combination represents a hash table.
When accessing items in a hash table, you just need to pass the input(key) passed to the hash function, and the value stored with that input will be retrieved by the hash function using its index.

While arrays and linked lists map data straight to memory, hash tables are smarter and use hash functions to intelligently figure out where to store the data.

Most programming languages come with hash tables already implemented.
In python, they're called `dictionaries`

Creating a hash table in python

```py
# create an empty hash table
book = new dict()  # or book = {}


# add new items 
book["apple"] = 0.67
book["milk"]  = 1.49


# look up an item in the hash table
# using "milk" as key to look up its value
print(book["milk"])
#  returns 1.49(value)
```

## Use Cases

1. For lookups  
2. For preventing duplicate entries, since keys are unique
3. For caching. Hash tables can store cache data, which can be quickly retrieved whenever needed

## Collisions

Sometimes hash functions do not always efficiently assign keys to slots in the array.
It's possible that multiple keys can be assigned to the same slot by a hash function, causing **collisions**.

A work-around for collisions is to start a new linked list in slot that has multiple keys assigned to it, so that previous key's values are not overwritten.
However, performance can get slow if there are too many keys assigned to the same slot, since linked lists are slow to search through.

A good hash function, however, will give a few collisions

## Performance

In the average case, hash tables take `O(1)` time for everything.
In the worst case however, they take `O(n)` time. How?
Hash tables are as fast as arrays at searching(getting a value at an index), and as fast as linked lists at inserts and deletes.

The worst case performance for hash tables happen when there are collisions.
To avoid collisions in hash tables you need two things:

- a good load factor
- a good hash function

### Load factor

This refers to the number of items in the hash table divided by the total number of slots. E.g. a load factor of `2/5` means out of 5 empty slots in a hash table, 2 are occupied.

Having a load factor > 1 means there are more items than slots, and therefore more slots need to be added. Known as ***resizing***.

A good rule of thumb is to resize whenever load factor is greater than `0.7`.
To resize, you need to create a new array that's bigger than your original array and then re-insert all the items from the original array unto this new array. As a rule of thumb, the new array can be twice the size of the original one.

Ideally, you don't want to resize too often since they can be expensive.

### A good hash function

A good hash function distributes values in the array evenly, while a bad one groups values together and produces a lot of collisions.
