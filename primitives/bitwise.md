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

> **Note**: Unsigned data types don’t let you store negative numbers such as -273 because there’s no space for a sign in a regular bit pattern. Trying to do so would result in a compilation error, a runtime exception, or an integer overflow depending on the language used.

> Instead of the expected 9910, you get a negative value! The reason for this will become clear once you learn about the various [binary number representations](https://realpython.com/python-bitwise-operators/#binary-number-representations). For now, the quick-fix solution is to take advantage of the bitwise AND operator:

```Py
>>> ~a & 255    # bitmask
99
```

# Bitwise Shift Operators

## Left Shift
```Py
>>> a = 39          # 100111
>>> a << 1         # 1001110
78
>>> a << 2        # 10011100
156
>>> a << 3       # 100111000
312
```

> The left shift used to be a popular **optimization** technique because bit shifting is a single instruction and is cheaper to calculate than exponent or product. Today, however, compilers and interpreters, including Python’s, are quite capable of optimizing your code behind the scenes.

> **Note**: Don’t use the bit shift operators as a means of premature optimization in Python. You won’t see a difference in execution speed, but you’ll most definitely make your code less readable.

### Bitmasked Left Shift

> In most practical cases, you’ll want to constrain the length of a bit pattern to be a multiple of eight, which is the standard byte length. For example, if you’re working with a single byte, then shifting it to the left should discard all the bits that go beyond its left boundary.

```Py
>>> 39 << 3
312
>>> (39 << 3) & 255     # 8-bit bitmask
56
```
