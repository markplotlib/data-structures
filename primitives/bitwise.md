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

## NOT
```Py
>>> a = 156     # 10011100
>>> ~a
```
... one would expect `a` to be:
`99              # 01100011`

However, `a` ends up as:

```Py
>>> ~a
-157
```

> While the bitwise NOT operator seems to be the most straightforward of them all, you need to exercise extreme caution when using it in Python. Everything you’ve read so far is based on the assumption that numbers are represented with **unsigned** integers.

> Note: Unsigned data types don’t let you store negative numbers such as -273 because there’s no space for a sign in a regular bit pattern. Trying to do so would result in a compilation error, a runtime exception, or an integer overflow depending on the language used.

> Instead of the expected 9910, you get a negative value! The reason for this will become clear once you learn about the various [binary number representations](https://realpython.com/python-bitwise-operators/#binary-number-representations). For now, the quick-fix solution is to take advantage of the bitwise AND operator:

```Py
>>> ~a & 255    # bitmask
99
```
