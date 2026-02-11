import pytest
from app.structures.linked_list import LinkedList
from app.structures.queue import Queue

class TestLinkedList:
    def test_add_and_iter(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        assert list(ll) == [1, 2, 3]

    def test_search(self):
        ll = LinkedList()
        ll.add("a")
        ll.add("b")
        assert ll.search("a") is True
        assert ll.search("c") is False

    def test_delete(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        
        ll.delete(1)
        assert list(ll) == [2, 3]
        
        ll.delete(3)
        assert list(ll) == [2]
        
        ll.delete(99)
        assert list(ll) == [2]

        ll.delete(2)
        assert list(ll) == []

    def test_empty_list(self):
        ll = LinkedList()
        assert list(ll) == []
        assert ll.search(1) is False
        ll.delete(1)    

class TestQueue:
    def test_add_remove(self):
        q = Queue()
        q.add(1)
        q.add(2)
        assert q.remove() == 1
        assert q.remove() == 2
        assert q.remove() is None

    def test_peek(self):
        q = Queue()
        assert q.peek() is None
        q.add(10)
        assert q.peek() == 10
        q.add(20)
        assert q.peek() == 10

    def test_is_empty(self):
        q = Queue()
        assert q.is_empty() is True
        q.add(1)
        assert q.is_empty() is False

    def test_search(self):
        q = Queue()
        q.add("x")
        assert q.search("x") is True
        assert q.search("y") is False

    def test_delete(self):
        q = Queue()
        q.add(1)
        q.add(2)
        q.delete(1)
        assert list(q) == [2]
        q.delete(99) 
        assert list(q) == [2]
