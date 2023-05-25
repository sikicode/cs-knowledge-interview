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
- split
    ```python
    txt = "I have an apple"
    lst = txt.split(" ")
    ```
5. Handling digits input
- pow(2, 31) for integer overflow/underflow check
- s[n].isdigit() to check if a character is a digit [0-9], use int() to turn digit to integer to handle.
6. [break and continue](https://www.programiz.com/python-programming/break-continue)
7. [yield](https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/)
8. [random.choice() O(logn)](https://www.w3schools.com/python/ref_random_choice.asp)
9. zip(): zip elements in a tuple and return
10. map(): map a function to iterable
11. hash(): returns hash value of an object (if it has one)
12. enumerate(object, start_index<optional>) returns a enumerate object, each item is a tuple (index, value), dict will be (index, key), O(1) time
13. sort(reverse=False, key=<mykey>): see [sorting](..%2Falgorithms%2Fsorting)