def tree_by_levels(node):
    if not node:
        return []
    result = []
    queue = [node]
    while queue:
        n = queue.pop(0)
        result.append(n.value)
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)
    return result