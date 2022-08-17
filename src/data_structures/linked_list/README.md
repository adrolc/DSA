# Linked List

In computer science, a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions. A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality compared to linked lists.

![alt text](docs/linked_list.png)

## Node insertion operation

![alt text](docs/linked_list_insert.png)

## Node removal operation

![alt text](docs/linked_list_remove.png)


*source:* [Wikipedia](https://en.wikipedia.org/wiki/Linked_list)


# Complexity

|            |        | Beginning        | End                                                  | Middle                |                  |
|------------|--------|------------------|------------------------------------------------------|-----------------------|------------------|
| Operation  | Access | Insert or Delete | Insert or Delete                                     | Insert or Delete      | Space Complexity |
| Complexity | Θ(n)   | Θ(1)             | Θ(1), known end element<br>Θ(n), unknown end element | Access time + Θ(1) | Θ(n)             |