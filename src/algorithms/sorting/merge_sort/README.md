# Merge sort

Merge sort (also commonly spelled as mergesort) is an efficient, general-purpose, and comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output. Merge sort is a divide-and-conquer algorithm that was invented by John von Neumann in 1945.

Conceptually, a merge sort works as follows:
* Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).

* Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

![alt text](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

*source:* [Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)


# Complexity

| Algorithm  | Best        | Average     | Worst       | Space |
|------------|-------------|-------------|-------------|-------|
| Merge sort | Ω(n log(n)) | Θ(n log(n)) | O(n log(n)) | O(n)  |