class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add_to_tail(self, value):
        on = self

        while on.next:  # traverse list while the current Node has next value
            print(f"{value} inserted after {on.next.value}")
            on = on.next  # assign next value to current Node to step forward

        on.next = Node(value)  # add value to end of list
        print(f"Inserted {on.next.value}")

    def get_at_index(self, index):
        on = self

        while on and index:
            on = on.next
            index = index - 1

        if on:
            return on.value
        else:
            return False


node = Node(4)
node.add_to_tail(5)
node.add_to_tail(6)

print(node.get_at_index(0))
# print(node.get_at_index(1))
# print(node.get_at_index(2))


# print(node.value)  # 4
# print(node.next.value)  # 5
# print(node.next.next.value)  # 6
# print(node.next.next.next.value)  # None
