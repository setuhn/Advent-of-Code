import re
import timeit
start = timeit.default_timer()

class Workflow():
    def __init__(self, name, refuse, logic, root = None) -> None:
        self.name = name
        self.refuse = refuse
        self.logic = logic
        self.root = root

    def evaluate(self, part):
        for evaluation in self.logic:
            out = self.refuse

            if (evaluation[1] == '<' and part[evaluation[0]] < evaluation[2]) or (evaluation[1] == '>' and part[evaluation[0]] > evaluation[2]):
                out =  evaluation[3]
                break
            
        return (True, out) if out in ['A', 'R'] else (False, out)

def calculate_sum_rating_scores(accepted_parts):
    return sum([sum([rating for rating in part.values()]) for part in accepted_parts])

def update_ranges(ratings_range, evaluation):
    rating, comparison, num, _ = evaluation

    if comparison == '<':
        ratings_range[rating].intersection_update(range(1, num))

    elif comparison == '>':
        ratings_range[rating].intersection_update(range(num + 1, 4001))

# Inspiration from day 10 for the area calculation
if __name__ == '__main__':

    regex_tag_end = re.compile(r'(\w+){.*,(\w+)}')
    regex_logic = re.compile(r'(\w+)([<>])(\d+):(\w+)')
    regex_parts = re.compile(r'(\w+)=(\d+)')

    workflows_dict = {}
    parts_list_dict = []

    with open(f'day_19.1-test.txt') as data:
        workflows_list, parts_list = [chunk.split('\n') for chunk in data.read().strip().split('\n\n')]

    for workflow in workflows_list:
        name, refuse = regex_tag_end.match(workflow).groups()
        logic = [(tag, comparison, int(num), out) for tag, comparison, num, out in regex_logic.findall(workflow)]

        workflows_dict[name] = Workflow(name, refuse, logic)

    for part in parts_list:
        part_dict = {}

        for tag, value in regex_parts.findall(part):
            part_dict[tag] = int(value)

        parts_list_dict.append(part_dict)

    accepted_parts = []

    for part in parts_list_dict:
        finished = False
        workflow_name = 'in'

        while not finished:
            finished, workflow_name = workflows_dict[workflow_name].evaluate(part)

        if workflow_name == 'A':
            accepted_parts.append(part)

    print(f'Answer part 1: {calculate_sum_rating_scores(accepted_parts)}')
    

    # Part 2: figure out the possible ranges for each rating -> work in reverse -> build a tree and walk back from each 'A' leaves (golden leaves)

    golden_leaves = []
    for workflow in workflows_dict.values():
        for evaluation in workflow.logic:
            if evaluation[-1] not in ['A', 'R']:
                workflows_dict[evaluation[-1]].root = workflow.name

            elif evaluation[-1] == 'A':
                golden_leaves.append([workflow.name, evaluation])

        if workflow.refuse not in ['A', 'R']:
            workflows_dict[workflow.refuse].root = workflow.name

        elif workflow.refuse == 'A':
                golden_leaves.append([workflow.name, workflow.refuse])
            
    ratings_range_all = []

    for leaf in golden_leaves:
        print(leaf, workflows_dict[leaf[0]].logic)
        ratings_range = {
            'x': set(range(1, 4001)),
            'm': set(range(1, 4001)),
            'a': set(range(1, 4001)),
            's': set(range(1, 4001))
        }
        
    #     current_name, evaluation = leaf
    #     update_ranges(ratings_range, evaluation)
    #     root = workflows_dict[current_name].root

    #     while root:
            
    #         evaluation = [evaluation for evaluation in workflows_dict[root].logic if current_name in evaluation]

    #         if evaluation:
    #             print(evaluation)
    #             evaluation = evaluation[0]
    #             update_ranges(ratings_range, evaluation)
            
    #         elif workflows_dict[root].refuse == current_name:
    #             print('refuse')
    #         else:
    #             print('WHAT', root, workflows_dict[root].logic, current_name)

    #             break

    #         root, current_name = workflows_dict[root].root, root

            

    # combination = 1
    # for r in ratings_range:
    #     print(r, min(ratings_range[r]), max(ratings_range[r]))
    #     combination *=  max(ratings_range[r]) - min(ratings_range[r])

    # print(combination)
    # print(combination < 167409079868000)

    # print(f'Answer part 2: {None}')
    # print(f'Time :{timeit.default_timer() - start} s')
