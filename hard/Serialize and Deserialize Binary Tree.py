class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(data, pointer):
    if pointer >= len(data) or data[pointer] is None:
        return None, pointer
    node = TreeNode(data[pointer])
    node.left, pointer = create_tree(data, pointer+1)
    node.right, pointer = create_tree(data, pointer+1)
    return node, pointer


def from_tree_to_data(root):
    if root is None:
        return [None]
    data = [root.val]
    data += from_tree_to_data(root.left)
    data += from_tree_to_data(root.right)
    return data


def from_list_to_string(l):
    return " ".join([str(x) for x in l])


def from_string_to_list(s):
    splited_s = s.split()
    for i in range(len(splited_s)):
        if splited_s[i] == 'None':
            splited_s[i] = None
        else:
            splited_s[i] = int(splited_s[i])
    return splited_s


def serialize(root):
    data = from_tree_to_data(root)
    return from_list_to_string(data)


def deserialize(data):
    converted_data = from_string_to_list(data)
    tree, pointer = create_tree(converted_data, 0)
    return tree


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5


data_tree = "1 2 None None 3 4 None None 5 None None"
data_tree2 = from_list_to_string([1,2,None, None, 3, None, None])
# print(serialize(node1))
print(deserialize(data_tree))





