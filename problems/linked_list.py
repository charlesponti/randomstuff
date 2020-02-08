class Home:
    def __init__(self, value):
        self.value = value
        self.next_owner = None

    def add_to_tail(self, value):
        on = self

        while on.next:  # traverse list while the current Node has next value
            # print(f"{value} inserted after {on.next.value}")
            on = on.next  # assign next value to current Node to step forward

        on.next = Node(value)  # add value to end of list
        # print(f"Inserted {on.next.value}")

    def get_at_index(self, index):
        on = self

        while on and index:  # traverse list until on node and index not 0
            on = on.next  # assign to next item in list
            index = index - 1  # decrement until at index

        if on:
            return on.value
        else:
            return False

    def add_at_index(self, value, index=0):
        on = self

        while on and index:
            on = on.next
            index = index - 1

        if on:
            on.value = value
        else:
            return False


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add_to_tail(self, value):
        on = self

        while on.next:  # traverse list while the current Node has next value
            # print(f"{value} inserted after {on.next.value}")
            on = on.next  # assign next value to current Node to step forward

        on.next = Node(value)  # add value to end of list
        # print(f"Inserted {on.next.value}")

    def get_at_index(self, index):
        on = self

        while on and index:  # traverse list until on node and index not 0
            on = on.next  # assign to next item in list
            index = index - 1  # decrement until at index

        if on:
            return on.value
        else:
            return False

    def add_at_index(self, value, index=0):
        on = self

        while on and index:
            on = on.next
            index = index - 1

        if on:
            on.value = value
        else:
            return False


node = Node(4)
node.add_to_tail(5)
node.add_to_tail(6)


def print_nodes_until_index(node: Node, index: int):
    for idx in range(index + 1):
        print(node.get_at_index(idx))


# print_nodes_until_index(node, 2)

node.add_at_index(15, index=1)
# print(node.get_at_index(1))
print_nodes_until_index(node, 2)
