import re
from operator import mul
from functools import reduce
import timeit
start = timeit.default_timer()

class Workflow():
    def __init__(self, name, logic, root = None) -> None:
        self.name = name
        self.logic = logic
        self.root = root

    def evaluate(self, part):
        for evaluation in self.logic[:-1]:
            out = self.logic[-1]

            if (evaluation[1] == '<' and part[evaluation[0]] < evaluation[2]) or (evaluation[1] == '>' and part[evaluation[0]] > evaluation[2]):
                out =  evaluation[3]
                break
            
        return (True, out) if out in ['A', 'R'] else (False, out)

def calculate_sum_rating_scores(accepted_parts):
    return sum([sum([rating for rating in part.values()]) for part in accepted_parts])

def update_ranges(ratings_range, evaluation, sense = True):
    rating, comparison, num, _ = evaluation

    if sense:
        if comparison == '<':
            ratings_range[rating].intersection_update(range(0, num))

        elif comparison == '>':
            ratings_range[rating].intersection_update(range(num + 1, 4001))
    
    else:
        if comparison == '<':
            ratings_range[rating].intersection_update(range(num, 4001))

        elif comparison == '>':
            ratings_range[rating].intersection_update(range(0, num + 1))

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

        workflows_dict[name] = Workflow(name, logic + [refuse])

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
    
    # # Part 2: figure out the possible ranges for each rating -> work in reverse -> build a tree and walk back from each 'A' leaves (golden leaves)

    golden_leaves = []

    for workflow in workflows_dict.values():

        for evaluation in workflow.logic[:-1]:

            if evaluation[-1] not in ['A', 'R']:
                workflows_dict[evaluation[-1]].root = workflow.name

            elif evaluation[-1] == 'A':
                golden_leaves.append([workflow.name, evaluation])

        if workflow.logic[-1] not in ['A', 'R']:
            workflows_dict[workflow.logic[-1]].root = workflow.name

        elif workflow.logic[-1] == 'A':
                golden_leaves.append([workflow.name, workflow.logic[-1]])

    # print(golden_leaves)
            
    accepted_paths = []


    for leaf in golden_leaves:
        ratings_range = {
            'x': set(range(0, 4001)),
            'm': set(range(0, 4001)),
            'a': set(range(0, 4001)),
            's': set(range(0, 4001))
        }   
        # print(leaf, workflows_dict[leaf[0]].logic, workflows_dict[workflows_dict[leaf[0]].root].logic)
        current_name, evaluation = leaf

        # If evaluation contains a rule, updates the range
        if evaluation != 'A':
            update_ranges(ratings_range, evaluation)

        # Otherwise, update the opposite of the logic
        else:
            for eval in workflows_dict[current_name].logic[:-1]:
                update_ranges(ratings_range, eval, False)


        root = workflows_dict[current_name].root

        while root:
            
            evaluation = [evaluation for evaluation in workflows_dict[root].logic if current_name in evaluation]

            if evaluation:
                # print(evaluation)
                evaluation = evaluation[0]
                
                 # If evaluation contains a rule (all except last one), updates the range
                if evaluation != workflows_dict[root].logic[-1]:
                    update_ranges(ratings_range, evaluation)

                # Otherwise, update the opposite of the logic (last element of the logic)
                else:
                    for eval in workflows_dict[root].logic[:-1]:
                        update_ranges(ratings_range, eval, False)

            root, current_name = workflows_dict[root].root, root
        
        accepted_paths.append(ratings_range)

    # For each rating range, compare them (difference) to the ratings main. if the rating is not completely encompassed 
    # in the rating main, calculate the combination with all the rating ranges but replace the non encosed one with the difference
    # Only do this once. Add differences for all the ratings to the ratings main 
    
    # The first paths can be directly added and its combinations directly calculated
    ratings_range_main = accepted_paths[0]
    combination = reduce(mul,[max(rating) - min(rating) for rating in ratings_range_main.values()])

    # Iterate over all the possible paths for success
    for path in accepted_paths[1:]:
        # In these paths, iterate over the ranges for each rating
        for label in ratings_range:
            # If a range in not entirely encompassed in the main ratings_range
            if ratings_range_main[label].difference(path[label]) != 0:
                # iterate over all the ranges of this path to calculate the combination replacing only the found 
                for k in path:
                    break

        print()
    
    # print(combination, combination == 167409079868000, 4000**4)
            

    # # combination = 1
    # # for r in ratings_range:
    # #     print(r, min(ratings_range[r]), max(ratings_range[r]))
    # #     combination *=  max(ratings_range[r]) - min(ratings_range[r])

    # # print(combination)
    # # print(combination < 167409079868000)

    # # print(f'Answer part 2: {None}')
    # # print(f'Time :{timeit.default_timer() - start} s')
