import re

class Node:
    def __init__(self, name, weight=None, children=None, parent=None):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = parent
        self.children_weight = None

def build_tree(filename):
    Tree = {}
        
    with open(filename) as data:
        for line in data.readlines():
            line = line.strip()
            # print(line)
            name, weight, children = re.match(r'(\w+)\s+\((\d+)\)(?:\s+->\s+)?(.+)?', line).groups()

            weight = int(weight)
            name = name.strip()

            if children:
                children = [child.strip() for child in children.split(',')]

                for child in children:

                    if child not in Tree.keys():
                        Tree[child] = Node(name)

                    Tree[child].parent = name

            if name not in Tree.keys():
                Tree[name] = Node(name, weight, children = children)

            else:
                Tree[name].weight = weight
                Tree[name].children = children

    node = Tree[name]
    while node.parent != None:
        node = Tree[node.parent]

    origin = node

    return (Tree, origin)

def calculate_weights(node):
    if not node.children_weight:
        node.children_weight = 0
    
    if node.children:
        children_weight_lst = []

        for child in node.children:
            children_weight_lst.append(calculate_weights(Tree[child]))

        children_weight_set = set(children_weight_lst)

        if len(children_weight_set) > 1:
            print(node.name)
            children_weight_freq = {children_weight_lst.count(x):x for x in children_weight_set}

            goal_weight = children_weight_freq[len(children_weight_lst) - 1]
            current_weight = children_weight_freq[1]

            change_weight = goal_weight - current_weight

            print(node.weight, change_weight)

        node.children_weight = sum(children_weight_lst)
        node.weight += node.children_weight
        
    return node.weight

def print_Tree():
    for node in Tree.keys():
        print(f'{node} ({Tree[node].weight}, {Tree[node].children_weight}): {Tree[node].children}')

Tree, origin = build_tree('2017/input_7_test')

print(f'Answer to part 1: {origin.name}')

calculate_weights(origin)

# print_Tree()
