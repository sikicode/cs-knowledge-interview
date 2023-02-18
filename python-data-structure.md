1. Is Python call by reference or call by value?
   <br>Python utilizes a system, which is known as “Call by Object Reference” or <mark>“Call by assignment”</mark>. In the event that you pass arguments like whole numbers, strings or tuples to a function, the passing is like call-by-value because you can not change the value of the immutable objects being passed to the function. Whereas passing mutable objects can be considered as call by reference because when their values are changed inside the function, then it will also be reflected outside the function.
<br>
2. Swap values for two variables: <br>&nbsp;&nbsp;&nbsp;&nbsp;no temp variable needed in python a, b, c = c, b, a
3. Slicing syntax:
```python
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
a[start:stop:step] # start through not past stop, by step
```
4. Check palindrome: sub == sub[::-1] Reference: leetcode 4
5. Iteration vs Recursion (e.g. binary search)
<br>Recursion solves the problem by function itself, feed the result back into function.
<br>While Iteration use loops to repeat a set of instructions
6. Sets 
<br> - Elements cannot be duplicated. 
<br> - Elements are immutable, but set itself mutable
<br> - No indexing/slicing since no index
   ```python
   set_example = set() 
   set_example2 = {1, 2, 3}
   # cannot duplicate no change
   set_example.add(1)
   set_example.remove(1)
   ```
