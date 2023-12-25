import re
from collections import deque
import timeit
start = timeit.default_timer()

class Workflow():
    def __init__(self, name, logic, root = None) -> None:
        self.name = name
        self.logic = logic
        self.root = root

def get_golden_leaves(workflows_dict):
    golden_leaves = []

    for workflow in workflows_dict.values():

        for evaluation in workflow.logic[:-1]:

            if evaluation[-1] not in ['A', 'R']:
                workflows_dict[evaluation[-1]].root = workflow.name

            elif evaluation[-1] == 'A':
                golden_leaves.append([workflow.name, [evaluation]])

        if workflow.logic[-1] not in ['A', 'R']:
            workflows_dict[workflow.logic[-1]].root = workflow.name

        elif workflow.logic[-1] == 'A':
                golden_leaves.append([workflow.name, workflow.logic[-1]])

    return golden_leaves

# get ranges_list by removing the non-possible ratings
def get_range(node_name, evaluation):
    rating_name, comparison, num, next_node_name = evaluation

    sense = True if node_name == next_node_name else False

    if sense:
        if comparison == '<':
            return {rating_name: set(range(0, num))}

        else:
            return {rating_name: set(range(num + 1, 4001))}
    
    else:
        if comparison == '<':
            return {rating_name: set(range(num, 4001))}

        else:
            return {rating_name: set(range(0, num + 1))}

if __name__ == '__main__':

    regex_tag_end = re.compile(r'(\w+){.*,(\w+)}')
    regex_logic = re.compile(r'(\w+)([<>])(\d+):(\w+)')

    workflows_dict = {}

    with open(f'day_19.1-test.txt') as data:
        workflows_list, parts_list = [chunk.split('\n') for chunk in data.read().strip().split('\n\n')]

    for workflow in workflows_list:
        name, refuse = regex_tag_end.match(workflow).groups()
        logic = [(tag, comparison, int(num), out) for tag, comparison, num, out in regex_logic.findall(workflow)]

        workflows_dict[name] = Workflow(name, logic + [refuse])
    
    # # Part 2: figure out the possible ranges for each rating -> work in reverse -> build a tree and walk back from each 'A' leaves (golden leaves)

    golden_leaves = get_golden_leaves(workflows_dict)
            
    accepted_paths = {}

    # Construct tree of possible paths for acceptable ratings
    for leaf in golden_leaves:
        current_name, evaluation = leaf
        root = workflows_dict[current_name].root
        
        if evaluation == workflows_dict[current_name].logic[-1]:
            evaluation = workflows_dict[current_name].logic[:-1]
        
        if current_name not in accepted_paths:
            accepted_paths[current_name] = {}

        if 'A' not in accepted_paths[current_name]:
            accepted_paths[current_name]['A'] = [get_range('A', eval) for eval in evaluation]

            
        while root:
            
            evaluation = [evaluation for evaluation in workflows_dict[root].logic if current_name in evaluation]

            if evaluation[0] == workflows_dict[root].logic[-1]:
                evaluation = workflows_dict[root].logic[:-1]
            
            if root not in accepted_paths:
                accepted_paths[root] = {}

            if current_name not in accepted_paths[root]:
                accepted_paths[root][current_name] = [get_range(current_name, eval) for eval in evaluation]


            root, current_name = workflows_dict[root].root, root

    combination = 0
    q = deque()
    q.append([['in'], {
        'x': set(range(1, 4001)),
        'm': set(range(1, 4001)),
        'a': set(range(1, 4001)),
        's': set(range(1, 4001))
    }])
    for path in accepted_paths:
        print(path, accepted_paths[path].keys())
    # # Traverse all the possible paths and record the ranges
    # while q:
    #     history, ranges = q.popleft()
    #     current_node = history[-1]

    #     for path in accepted_paths[current_node]:
    #         next_q = [history + [path], 'ratings']

    #         if path == 'A':
    #             print(next_q)
    #             continue
    #         else:
    #             q.append(next_q)

        # print(path, accepted_paths[path].keys(), len(accepted_paths[path]))
