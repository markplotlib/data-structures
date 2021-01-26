Source of Inspiration: [Real Python](https://realpython.com/python-bitwise-operators/)

# bitwise operators
```
a & b
a | b
a ^ b
~a
a << n
a >> n
```

## augmented assignments (for *binary* operators)
```
a &= b
a |= b
a ^= b
a <<= n
a >>= n
```

### How Computers Use Binary
In Python, strings are represented as arrays of Unicode code points. To reveal their ordinal values, call `ord()` on each of the characters:

```Py
>>> ord(u), ord(o)
(117, 111)
```

char u = decimal 117 = binary 1110101.

char o = decimal 111 = binary 1101111.

```Py
>>> (127).bit_length()
7
>>> (128).bit_length()
8
```

# Bitwise Logical Operators
```Py
>>> a = 156     # 10011100
>>> b = 52      # 00110100
>>> a & b
20              # 00010100
>>> a | b
188             # 10111100
```

## XOR
```Py
def xor(a, b):
    return (a and not b) or (not a and b)

>>> a = 156     # 10011100
>>> b = 52      # 00110100
>>> a ^ b
168             # 10101000
```
