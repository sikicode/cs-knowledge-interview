1. Comparison
- <b>List is a collection which is ordered and changeable. Allows duplicate members.</b>
- <b>Tuple is a collection which is ordered and unchangeable. Allows duplicate members.</b>
- <b>Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.</b>
- <b>Dictionary is a collection which is ordered** and changeable. No duplicate members.</b>

2. Lists https://www.w3schools.com/python/python_lists.asp
- List access O(1) while set access O(n)
- List can hold various types but array can only hold one type
- 2D array initialization:
    ```
    [[''] * numCols for _ in range(numRows)]
    ```
3. Sets https://www.w3schools.com/python/python_sets.asp
- Set access O(n) while list access O(1)
4. Tuples: https://www.w3schools.com/python/python_tuples.asp
5. Dictionaries: https://www.w3schools.com/python/python_dictionaries.asp