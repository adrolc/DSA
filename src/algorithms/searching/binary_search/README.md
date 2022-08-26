# Binary search

Binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a **sorted array**. Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array

Binary search runs in logarithmic time in the worst case, making *O(log n)* comparisons, where *n* is the number of elements in the array. Binary search is faster than linear search except for small arrays. However, the array must be sorted first to be able to apply binary search. There are specialized data structures designed for fast searching, such as hash tables, that can be searched more efficiently than binary search. However, binary search can be used to solve a wider range of problems, such as finding the next-smallest or next-largest element in the array relative to the target even if it is absent from the array.

# How it works
Binary search works on sorted arrays. Binary search begins by comparing an element in the middle of the array with the target value. If the target value matches the element, its position in the array is returned. If the target value is less than the element, the search continues in the lower half of the array. If the target value is greater than the element, the search continues in the upper half of the array. By doing this, the algorithm eliminates the half in which the target value cannot lie in each iteration.

*source:* [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

![alt text](https://c.tenor.com/Jl0YrqxnHmAAAAAd/binary-search-sequence-search.gif)



# Complexity

| Algorithm     | Best | Average  | Worst    | Space |
|---------------|------|----------|----------|-------|
| Binary search | Ω(1) | Θ(log n) | O(log n) | O(1)  |