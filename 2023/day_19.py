import re

class Workflow():
    def __init__(self, name, refuse, logic) -> None:
        self.name = name
        self.refuse = refuse
        self.logic = logic

    def evaluate(self, part):
        for evaluation in self.logic:
            out = self.refuse

            if (evaluation[1] == '<' and part[evaluation[0]] < evaluation[2]) or (evaluation[1] == '>' and part[evaluation[0]] > evaluation[2]):
                out =  evaluation[3]
                break
            
        return (True, out) if out in ['A', 'R'] else (False, out)

def calculate_sum_rating_scores(accepted_parts):
    return sum([sum([rating for rating in part.values()]) for part in accepted_parts])

# Inspiration from day 10 for the area calculation
if __name__ == '__main__':

    regex_tag_end = re.compile(r'(\w+){.*,(\w+)}')
    regex_logic = re.compile(r'(\w+)([<>])(\d+):(\w+)')
    regex_parts = re.compile(r'(\w+)=(\d+)')

    workflows_dict = {}
    parts_list_dict = []

    with open(f'day_19.txt') as data:
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
        wf = 'in'

        while not finished:
            finished, wf = workflows_dict[wf].evaluate(part)

        if wf == 'A':
            accepted_parts.append(part)

    print(f'Answer part 1: {calculate_sum_rating_scores(accepted_parts)}')

    # Part 2: figure out the possible ranges for each rating -> work in reverse -> build a tree and walk back from each 'A' leaves
