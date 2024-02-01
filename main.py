class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value(root.right)
        root.right = delete(root.right, root.val)
    return root


def min_value(node: Node):
    current = node
    while current.left:
        current = current.left
    return current.val


def max_value(node: Node):
    current = node
    while current.right:
        current = current.right
    return current.val


def sum_values_recursive(node: Node) -> int:
    if node is None:
        return 0

    values_sum = node.val
    values_sum += sum_values_recursive(node.left)
    values_sum += sum_values_recursive(node.right)

    return values_sum


def sum_values_iterable(node: Node) -> int:
    if node is None:
        return 0

    values_sum = 0
    stack = [node]
    while stack:
        current = stack.pop()
        values_sum += current.val
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return values_sum


if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    print(root)

    print("\nTask 1:")
    print("В бінарному дереві пошуку найменший елемент завжди найлівіший")
    print(f"Min value: {min_value(root)}")

    print("\nTask 2:")
    print("В бінарному дереві пошуку найбільший елемент завжди нвйправіший")
    print(f"Max value: {max_value(root)}")

    print("\nTask 3:")
    print(f"Sum of values iterable: {sum_values_iterable(root)}")
    print(f"Sum of values recursive: {sum_values_recursive(root)}")
