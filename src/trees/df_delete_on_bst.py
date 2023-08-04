def delete(tree, target):
    if tree is None:
        return tree
    elif target < tree.value:
        tree.left = delete(tree.left, target)
    elif target > tree.value:
        tree.right = delete(tree.right, target)
    else:
        # case 1: target is a leaf
        if not tree.left and not tree.right:
            tree = None
        # case 2: target has one child
        elif not tree.left:
            tmp = tree.right
            tree.right = None
            tree = tmp
        elif not tree.right:
            tmp = tree.left
            tree.left = None
            tree = tmp
        # case 3: target has two children
        else:
            # find the minimum value in the right subtree
            # replace the target with the minimum value
            # delete the minimum value from the right subtree
            current = tree.right
            while current.left:
                current = current.left
            tree.value = current.value
            tree.right = delete(tree.right, current.value)


def df_delete(tree, target):
    delete(tree, target)
