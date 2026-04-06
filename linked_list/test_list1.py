import unittest

from listl import linked_list

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = linked_list()

    def tearDown(self):
        self.linked_list.destroy()

    def test_add(self):
        self.linked_list.add(1)
        self.assertEqual(self.linked_list.head.data, 1)
        self.linked_list.add(2)
        self.assertEqual(self.linked_list.head.data, 2)
        self.assertEqual(self.linked_list.head.next.data, 1)

    def test_append(self):
        self.linked_list.append(1)
        self.assertEqual(self.linked_list.head.data, 1)
        self.linked_list.append(2)
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.head.next.data, 2)

    def test_remove(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.remove()
        self.assertEqual(self.linked_list.head.data, 1)
        self.linked_list.remove()
        self.assertTrue(self.linked_list.is_empty())

    def test_remove_end(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.remove_end()
        self.assertEqual(self.linked_list.head.data, 2)
        self.assertTrue(self.linked_list.head.next is None)
        self.linked_list.remove_end()
        self.assertTrue(self.linked_list.is_empty())
    

if __name__ == '__main__':
    unittest.main()