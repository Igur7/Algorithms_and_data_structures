from rec2 import rec2_list

import unittest

class Test2WayLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = rec2_list()

    def tearDown(self):
        self.linked_list.destroy()

    def test_add(self):
        self.linked_list.add(1)
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.tail.data, 1)
        self.linked_list.add(2)
        self.assertEqual(self.linked_list.head.data, 2)
        self.assertEqual(self.linked_list.tail.data, 1)

    def test_append(self):
        self.linked_list.append(1)
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.tail.data, 1)
        self.linked_list.append(2)
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.tail.data, 2)

    def test_remove(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.remove()
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.tail.data, 1)
        self.linked_list.remove()
        self.assertTrue(self.linked_list.is_empty())

    def test_remove_end(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.remove_end()