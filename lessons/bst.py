class Node:
    def __init__(self, val, **kwargs):
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, *args, **kwargs):
        self.root = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                return self.right.insert(data)

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
