# Bubble sort

Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

![alt text](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

*source:* [Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)

In this implementation the `bound` variable is used to improve the efficiency. Specifies the location of the last swap, this means that all items after the last swap are already sorted and you don't have to compare them again.

For example:

input: [5, 2, 1, 3, 7, 12, 22, 55]

* Iteration 1: from 0 to n - 1:
    * [<span style="color:#00cec9">**5**</span>, <span style="color:#00cec9">**2**</span>, 1, 3, 7, 12, 22, 55]
    * [2, <span style="color:#00cec9">**5**</span>, <span style="color:#00cec9">**1**</span>, 3, 7, 12, 22, 55]
    * [2, 1, <span style="color:#00cec9">**5**</span>, <span style="color:#00cec9">**3**</span>, 7, 12, 22, 55] <span style="color:#ff7675">**last swap**</span>: arr[<span style="color:#00cec9">**2**</span>] <-> arr[<span style="color:#00cec9">**3**</span>]
    * ...
* Iteration 2: from 0 to <span style="color:#00cec9">**2**</span> (<span style="color:#ff7675">**last swap position**</span>)
  * [<span style="color:#00cec9">**2**</span>, <span style="color:#00cec9">**1**</span>, 3]<span style="color:#2d3436">, 5, 7, 12, 22, 55]</span> <span style="color:#ff7675">**last swap**</span>: arr[<span style="color:#00cec9">**0**</span>] <-> arr[<span style="color:#00cec9">**1**</span>]
* return: [1, 2, 3, 5, 7, 12, 22, 55]

Great, our array is sorted. As you may have noticed, during the first iteration, the last swap was between `arr[2]` and `arr[3]`. This means that all elements after `arr[2]` are sorted and you don't have to check them in the next iteration.

# Complexity

| Algorithm   | Best | Average          | Worst            | Space |
|-------------|------|------------------|------------------|-------|
| Bubble sort | Ω(n) | Θ(n<sup>2</sup>) | O(n<sup>2</sup>) | O(1)  |