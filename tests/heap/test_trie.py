from src.heap.trie import Trie


def test_trie():
    trie = Trie()
    trie.insert("foo")
    trie.insert("fool")
    trie.insert("fool")
    trie.insert("foolish")
    trie.insert("foolish")
    trie.insert("bar")

    assert trie.find("fo") == [("fool", 2), ("foolish", 2), ("foo", 1)]

    trie.insert("foo")
    trie.insert("foo")
    assert trie.delete("fool") is True
    assert trie.delete("fool") is False

    assert trie.find("fo") == [("foo", 3), ("foolish", 2)]

    trie.insert("foolish")
    trie.insert("foolish")

    assert trie.find("fo") == [("foolish", 4), ("foo", 3)]
