## Hash Tables
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
book = new dict()

# add new items 
book["apple"] = 0.67
book["milk"]  = 1.49


# look up an item in the hash table
# using "milk" as key to look up its value
print(book["milk"])
#  returns 1.49(value)
```


