1. Array Manipulation
- 2D array initialization:
    ```
    [[''] * numCols for _ in range(numRows)]
    ```
2. Sets
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
