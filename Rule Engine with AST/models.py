class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left            # Left child for operator node
        self.right = right          # Right child for operator node
        self.value = value          # Value for operand node (e.g., {"field": "age", "op": ">", "val": 30})

    def __repr__(self):
        return f"Node({self.node_type}, {self.value}, {self.left}, {self.right})"
