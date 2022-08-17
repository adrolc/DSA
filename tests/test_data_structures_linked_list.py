import unittest

from data_structures.linked_list.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList([5, 'foo', 10])
    
    def _test_equal_list(self, expected_output: list):
        self.assertEqual(list(self.linked_list), expected_output)

    def test_list_initialization(self):
        self._test_equal_list([5, 'foo', 10])
        self.assertEqual(len(self.linked_list), 3)
        self.assertEqual(self.linked_list.get_head(), 5)
        self.assertEqual(self.linked_list.get_tail(), 10)
    
    def test_list_iteration(self):
        iteration = iter(self.linked_list)
        self.assertEqual(next(iteration), 5)
        self.assertEqual(next(iteration), 'foo')
        self.assertEqual(next(iteration), 10)
        with self.assertRaises(StopIteration):
            next(iteration)

    def test_list_representation(self):
        self.assertEqual(repr(self.linked_list), "LinkedList<5, 'foo', 10>")
        self.linked_list.insert(-10)
        self.assertEqual(repr(self.linked_list), "LinkedList<5, 'foo', 10, -10>")
        self.linked_list.remove_first()
        self.assertEqual(repr(self.linked_list), "LinkedList<'foo', 10, -10>")
        self.linked_list.insert_after(10, 99)
        self.assertEqual(repr(self.linked_list), "LinkedList<'foo', 10, 99, -10>")
    
    def test_list_length(self):
        self.assertEqual(len(self.linked_list), 3)
        self.linked_list.insert(100)
        self.assertEqual(len(self.linked_list), 4)
        self.linked_list.insert_front(33)
        self.assertEqual(len(self.linked_list), 5)
        self.linked_list.insert_after(33, 55)
        self.assertEqual(len(self.linked_list), 6)
        self.linked_list.insert_before(33, 6)
        self.assertEqual(len(self.linked_list), 7)
        self.linked_list.remove(33)
        self.assertEqual(len(self.linked_list), 6)
        self.linked_list.remove_first()
        self.assertEqual(len(self.linked_list), 5)
        self.linked_list.remove_last()
        self.assertEqual(len(self.linked_list), 4)

    def test_list_getitem(self):
        self.assertEqual(self.linked_list[1], 'foo')
        self.assertEqual(self.linked_list[0], 5)
        with self.assertRaises(IndexError):
            self.linked_list[3]
        with self.assertRaises(IndexError):
            self.linked_list[-1]
    
    def test_list_setitem(self):
        self.linked_list[1] = 8
        self.assertEqual(self.linked_list[1], 8)
        with self.assertRaises(IndexError):
            self.linked_list[3] = 5
        with self.assertRaises(IndexError):
            self.linked_list[-1] = 5
    
    def test_list_contains(self):
        self.assertTrue(5 in self.linked_list)
        self.assertTrue('foo' in self.linked_list)
        self.assertTrue('22' not in self.linked_list)
        self.assertFalse(17 in self.linked_list)
        
    def test_list_get_head(self):
        self.assertEqual(self.linked_list.get_head(), 5)
        self.linked_list.insert_front('bar')
        self.assertEqual(self.linked_list.get_head(), 'bar')
        self.linked_list.remove_first()
        self.assertEqual(self.linked_list.get_head(), 5)

    def test_list_get_tail(self):
        self.assertEqual(self.linked_list.get_tail(), 10)
        self.linked_list.insert('bar')
        self.assertEqual(self.linked_list.get_tail(), 'bar')
        self.linked_list.remove_last()
        self.assertEqual(self.linked_list.get_tail(), 10)

    def test_list_insert(self):
        self.linked_list.insert(55)
        self._test_equal_list([5, 'foo', 10, 55])
        self.linked_list.insert('bar')
        self._test_equal_list([5, 'foo', 10, 55, 'bar'])
        self.linked_list.insert(3.5)
        self._test_equal_list([5, 'foo', 10, 55, 'bar', 3.5])

    def test_list_insert_front(self):
        self.linked_list.insert_front(55)
        self._test_equal_list([55, 5, 'foo', 10])
        self.linked_list.insert_front('bar')
        self._test_equal_list(['bar', 55, 5, 'foo', 10])
        self.linked_list.insert_front(3.5)
        self._test_equal_list([3.5, 'bar', 55, 5, 'foo', 10])

    def test_list_insert_before(self):
        self.linked_list.insert_before('foo', 1)
        self._test_equal_list([5, 1, 'foo', 10])
        self.linked_list.insert_before(10, 5)
        self._test_equal_list([5, 1, 'foo', 5, 10])
        self.linked_list.insert_before(5, 8)
        self._test_equal_list([8, 5, 1, 'foo', 5, 10])

    def test_list_insert_after(self):
        self.linked_list.insert_after('foo', 1)
        self._test_equal_list([5, 'foo', 1, 10])
        self.linked_list.insert_after(10, 5)
        self._test_equal_list([5, 'foo', 1, 10, 5])
        self.linked_list.insert_after(5, 8)
        self._test_equal_list([5, 8, 'foo', 1, 10, 5])

    def test_list_clear(self):
        self.linked_list.clear()
        self.assertEqual(repr(self.linked_list), "LinkedList<>")
        self.assertIsNone(self.linked_list.get_head())
        self.assertIsNone(self.linked_list.get_tail())
        self.assertEqual(len(self.linked_list), 0)
        self.assertTrue(self.linked_list.is_empty())
        self._test_equal_list([])
    
    def test_list_remove_first(self):
        self.linked_list.remove_first()
        self._test_equal_list(['foo', 10])
        self.linked_list.remove_first()
        self._test_equal_list([10])
        self.linked_list.remove_first()
        self._test_equal_list([])
        with self.assertRaises(IndexError):
            self.linked_list.remove_first()

    def test_list_remove_last(self):
        self.linked_list.remove_last()
        self._test_equal_list([5, 'foo'])
        self.linked_list.remove_last()
        self._test_equal_list([5])
        self.linked_list.remove_last()
        self._test_equal_list([])
        with self.assertRaises(IndexError):
            self.linked_list.remove_last()
    
    def test_list_remove(self):
        self.linked_list.remove('foo')
        self._test_equal_list([5, 10])
        self.linked_list.remove(5)
        self._test_equal_list([10])
        with self.assertRaises(KeyError):
            self.linked_list.remove(99)

    def test_list_reverse(self):
        self.linked_list.reverse()
        self._test_equal_list([10, 'foo', 5])
        self.linked_list.insert(3)
        self.linked_list.insert('bar')
        self.linked_list.reverse()
        self._test_equal_list(['bar', 3, 5, 'foo', 10])
    
    def test_list_find(self):
        index = self.linked_list.find('foo')
        self.assertEqual(index, 1)
        self.assertEqual(self.linked_list[index], 'foo')
        with self.assertRaises(KeyError):
            self.linked_list.find(55)
    
    def test_list_is_empty(self):
        self.assertFalse(self.linked_list.is_empty())
        self.linked_list.clear()
        self.assertTrue(self.linked_list.is_empty())


if __name__ == "__main__":
    unittest.main()