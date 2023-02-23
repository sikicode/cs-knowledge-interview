1. Comparison
- <b>List is a collection which is ordered and changeable. Allows duplicate members.</b> 
  https://www.w3schools.com/python/python_lists.asp
- <b>Tuple is a collection which is ordered and unchangeable. Allows duplicate members.</b>
  https://www.w3schools.com/python/python_tuples.asp
- <b>Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.</b>
  https://www.w3schools.com/python/python_sets.asp
- <b>Dictionary is a collection which is ordered** and changeable. No duplicate members.</b>
  https://www.w3schools.com/python/python_dictionaries.asp

2. Lists https://www.w3schools.com/python/python_lists.asp
- 2D array initialization:
    ```
    [[''] * numCols for _ in range(numRows)]
    ```

3. Sets https://www.w3schools.com/python/python_sets.asp
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