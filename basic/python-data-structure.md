1. Collections Comparison:
- Usage:
   - List is indexed, mutable, allows duplicate members.
   - Tuple is indexed, unmutable, allows duplicate members.
   - Set is unindexed, unmutable*, no duplicate members.
   - Dictionary is indexed** and mutable, no duplicate members.
- Time Complexity: [List, Dict and Set](https://www.geeksforgeeks.org/complexity-cheat-sheet-for-python-operations/)
<br>Related question: [380](https://leetcode.com/problems/insert-delete-getrandom-o1/solutions/455253/python-super-efficient-detailed-explanation/) - More explanation: [here](https://stackoverflow.com/questions/17539367/python-dictionary-keys-in-complexity)

2. [Lists:](https://www.w3schools.com/python/python_lists.asp)
- List can hold various types but array can only hold one type
- 2D array initialization:
    ```
    [[''] * numCols for _ in range(numRows)]
    ```
3. [Sets:](https://www.w3schools.com/python/python_sets.asp)
- Base implementation is HashTable (lookup/insert/delete O(1))
4. [Tuples:](https://www.w3schools.com/python/python_tuples.asp)
5. [Dictionaries:](https://www.w3schools.com/python/python_dictionaries.asp)