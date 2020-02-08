from problems.linked_list import Node


def test_get_length():
    node = Node(4)
    node.add_to_tail(5)
    node.add_to_tail(6)
    assert node.get_length() == 3
    node.add_to_tail(5)
    node.add_to_tail(6)
    assert node.get_length() == 5


def test_add_to_tail():
    node = Node(4)
    node.add_to_tail(5)
    node.add_to_tail(6)
    assert node.get_length() == 3


def test_get_at_index():
    node = Node(4)
    node.add_to_tail(5)
    node.add_to_tail(6)
    assert node.get_at_index(0) == 4
    assert node.get_at_index(1) == 5
    assert node.get_at_index(2) == 6
