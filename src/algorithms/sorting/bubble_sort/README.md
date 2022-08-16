# Bubble sort

Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

![alt text](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

*source:* [Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)

In this implementation the `bound` variable is used to improve the efficiency. Specifies the location of the last swap, this means that all items after the last swap are already sorted and you don't have to compare them again.

# Complexity

| Algorithm   | Best | Average          | Worst            | Space |
|-------------|------|------------------|------------------|-------|
| Bubble sort | Ω(n) | Θ(n<sup>2</sup>) | O(n<sup>2</sup>) | O(1)  |