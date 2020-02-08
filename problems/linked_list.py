from logging import info
from typing import Any, Union


class Node:
    """Node of a linked list

    :param value: value to assign to Node
    :type value: Any
    """

    def __init__(self, value):
        """Constructor method
        """
        self.value = value
        self.next = None

    def add_to_tail(self, value: Any) -> None:
        """Add value to end of linked list

        :param value: value to add at end of list
        :type value: any
        :return: `int` if value set, `False` otherwise
        :type: `int` or `False`
        """
        on = self

        while on.next:  # traverse list while the current Node has next value
            on = on.next  # move to next Node

        on.next = Node(value)  # add value to end of list

    def get_at_index(self, index) -> Union[int, bool]:
        """Get value at index

        :param index: index to get value at
        :type index: int
        :return: `int` if value set, `False` otherwise
        :type: `int` or `False`
        """
        on = self

        while on and index:  # traverse list until on node and index not 0
            on = on.next  # move to next Node
            index = index - 1  # decrement until at index

        if on:
            return on.value  # return current Node to list
        else:
            return False  # return false if list is shorter than index provided

    def add_at_index(self, value, index: int = 0) -> Union[None, bool]:
        """Set new value at index in list

        :param value: value to set at index
        :type value: Any
        :param index: index to set value to
        :type index: int
        :return: `None` if value set, `False` otherwise
        """
        on = self

        while on and index:
            on = on.next
            index = index - 1

        if on:
            on.value = value
        else:
            return False

    def get_length(self) -> int:
        """Get length of list

        :return: Length of the list
        :rtype: int
        """
        on = self
        counter = 1  # start at 1 because we're at the first Node

        while on.next:
            counter += 1  # increase counter
            on = on.next  # move to next Noded

        return counter
