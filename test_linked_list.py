import unittest
from app.structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_add_and_iter(self):
        ll = LinkedList()
        ll.add("station1")
        ll.add("station2")
        ll.add("station3")

        items = list(ll)
        self.assertEqual(items, ["station1", "station2", "station3"])

    def test_search(self):
        ll = LinkedList()
        ll.add("A")
        self.assertTrue(ll.search("A"))
        self.assertFalse(ll.search("Z"))

    def test_delete(self):
        ll = LinkedList()
        ll.add("A")
        ll.add("B")
        ll.delete("A")
        self.assertEqual(list(ll), ["B"])

if __name__ == "__main__":
    unittest.main()
