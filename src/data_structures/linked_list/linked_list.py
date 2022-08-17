from typing import Any, Generator

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return repr(self.data)


class LinkedList:
    def __init__(self, data: list[Any]=None):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0
        if data:
            self.length = len(data)
            node = Node(data=data.pop(0))
            self.head = node

            for d in data:
                node.next = Node(data=d)
                node = node.next
            self.tail = node

    def __iter__(self) -> Generator[Any, None, None]:
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self) -> str:
        return "LinkedList<" + ", ".join([repr(node) for node in self]) + ">"

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, index: int) -> Any:
        if index > -1 and index < len(self):
            for i, node_data in enumerate(self):
                if i == index:
                    return node_data
        raise IndexError("List index out of range")

    def __setitem__(self, index: int, data: Any) -> None:
        if index > -1 and index < len(self):
            node = self.head
            for _ in range(index):
                node = node.next
            node.data = data
            return None
        raise IndexError("List index out of range")
    
    def __contains__(self, data: Any) -> bool:
        for node_data in self:
            if node_data == data:
                return True
        return False

    def get_head(self) -> Any:
        if self.head:
            return self.head.data
        return None

    def get_tail(self) -> Any:
        if self.tail:
            return self.tail.data
        return None

    def insert(self, data: Any) -> None:
        """Insert a node at the end of the list"""
        if self.head is None:
            self.head = self.tail = Node(data=data)
        else:
            new_node = Node(data=data)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert_front(self, data: Any) -> None:
        """Insert a node at the start of the list"""
        if self.head is None:
            self.head = self.tail = Node(data=data)
        else:
            new_node = Node(data=data)
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert_before(self, target: Any, data: Any) -> None:
        """Insert before specified node"""
        if self.head:
            if self.head.data == target:
                self.insert_front(data)
                return
            else:
                prev_node = self.head
                current_node = self.head.next
                while current_node:
                    if current_node.data == target:
                        new_node = Node(data=data)
                        new_node.next = prev_node.next
                        prev_node.next = new_node
                        self.length += 1
                        return
                    prev_node = current_node
                    current_node = current_node.next
        raise KeyError(f"{repr(target)} does not exist")

    def insert_after(self, target: Any, data: Any) -> None:
        """Insert after specified node"""
        current_node = self.head
        while current_node:
            if current_node.data == target:
                if current_node == self.tail:
                    self.insert(data)
                    return
                else:
                    new_node = Node(data=data)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    self.length += 1
                    return
            current_node = current_node.next
        raise KeyError(f"{repr(target)} does not exist")

    def clear(self) -> None:
        """Remove all nodes from the list"""
        self.head = self.tail = None
        self.length = 0

    def remove_first(self) -> None:
        """Remove the first node from the list"""
        if self.head:
            if self.head == self.tail:
                self.clear()
            else:
                self.head = self.head.next
                self.length -= 1
        else:
            raise IndexError("LinkedList is empty")

    def remove_last(self) -> None:
        """Remove the last node from the list"""
        if self.tail:
            if self.tail == self.head:
                self.clear()
            else:
                current_node = self.head
                while current_node:
                    if current_node.next == self.tail:
                        self.tail = current_node
                        self.tail.next = None
                        self.length -= 1
                    current_node = current_node.next
        else:
            raise IndexError("LinkedList is empty")

    def remove(self, target: Any) -> None:
        """Remove specified node"""
        if self.head.data == target:
            self.remove_first()
            return

        if self.tail.data == target:
            self.remove_last()
            return

        current_node = self.head
        while current_node:
            if current_node.next:
                if current_node.next.data == target:
                    current_node.next = current_node.next.next
                    self.length -= 1
                    return
            current_node = current_node.next
        raise KeyError(f"{repr(target)} does not exist")

    def reverse(self) -> None:
        """Reverse the list in-place"""
        if self.head and self.head.next:
            reversedList = None
            next = None
            currentNode = self.head
            self.tail = self.head
            while currentNode:
                next = currentNode.next
                currentNode.next = reversedList
                reversedList = currentNode
                currentNode = next
            self.head = reversedList

    def find(self, data: Any) -> int:
        """Find index by node value"""
        for i, node_data in enumerate(self):
            if node_data == data:
                return i
        raise KeyError(f"{data} does not exist")

    def is_empty(self) -> bool:
        return len(self) == 0
