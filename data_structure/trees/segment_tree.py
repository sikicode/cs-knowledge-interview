# Use Cases: return sum between a range / update value for O(logn)
# For each node at index i, the left child is at index (2*i+1), right child at (2*i+2) and the parent is at  (⌊(i – 1) / 2⌋).

# class SegmentTree:
#
#     def __init__(self):
#         self.INPUT_SIZE = 1000    # input array's size
#         self.tree = [0] * (2 *)
