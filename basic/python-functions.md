1. range()
```python
range(n) will generate 0 to n-1
range(start, stop, step) will include start exclude stop
range(3,20,2) - 3,5,7,9...19
```
2. counter()
```python
>>> from collections import Counter

>>> # Use a string as an argument
>>> Counter("mississippi")
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```
3. ceil() and floor(): 
```python
math.ceil(n)
math.floor(n)
```
4. String Manipulation
- append: use "+=". e.g. str += "test string"
- join: turn char list into string(must be all chars)
```python
str = "".join(['a', 'b'])
```
- replace
```python
txt = "I like bananas"
x = txt.replace("bananas", "apples")
```
5. Handling digits input
- pow(2, 31) for integer overflow/underflow check
- s[n].isdigit() to check if a character is a digit [0-9], use int() to turn digit to integer to handle