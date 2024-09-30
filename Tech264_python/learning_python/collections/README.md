
![tuples , lists, sets , frozen.png](..%2F..%2Fimages%2Ftuples%20%2C%20lists%2C%20sets%20%2C%20frozen.png)


# What is slicing strings?
        - can return a range of characters by using slice syntax
        - specify the start index and the end index, separated by a colon, to return a part of the string 

### slice() - slice the string when u set the index 
### strip() - removes spaces from the beginning and end of the string but not in between.
### count() - helps count how many times a substring appears in a string.
### lower() - and upper() change the case of the entire string.
### capitalize() - capitalizes just the first letter of the string.
### replace() - substitutes one substring with another in the entire string.
### append() - add a single item to the end of the list 
### remove() - remove a specific element from a list 
### pop() - method is used to remove and return an element from a list at a specified index.



#  What is best practice when deciding what quotes to use around strings in Python?
   * Consistency --- stick to one style consistently throughout the code

# What is concatenation? Give a simple example with your code.
   * Concatenation --- process of joining 2 or more strings together using +
                   --- only can concatenate springs




# Tuples 

  * How are tuples similar to lists? 
        * ordered collections
        * multiple data type
        * indexing and slicing
        * duplicate elements
        * iterable 
        * length      

  * Are tuples immutable and what does this mean? 
        * tuples cant be changed once created(cant modify, add, remove)

  * What other data types are immutable? 
        * strings
        * numbers
        * tuples
        * frozen sets
        * booleans

  * What is a good use case for tuples? 
        * safety - tuples are immutable, they are safer to use for data that should not change during program execution
        * performance - generally more memory-efficient and faster
        * dictionary key - Tuples are hashable (since they are immutable), so they can be used as keys in dictionaries or elements in sets, unlike lists


# Dictionary 

```python
    my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"}
```
  * collection of key-value pair, each value is associated with a unique key, which act as an identifier

  * Accessing Dictionary Elements:
```python
    print(person["name"])  # Output: Alice
```


# Sets
  * an unordered and mutable collection of unique elements 
  * cannot contain duplicate elements 
  * not hashable

```python
my_set = {"apple", "banana", "cherry"}
```


# Frozen Sets:
   * are immutable and do not allow modification after creation 
   * Hashable, so they can be added to other sets or used as dictionary keys.

```python
frozen_set = frozenset(["apple", "banana", "cherry"])
```