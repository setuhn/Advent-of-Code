# check if the trial spring is compliant with the condition.
def is_right(spring, condition):
    pass

if __name__ == '__main__':
    
    with open(f'day_12.1-test.txt') as data:
        spring_fields = []

        for line in data.readlines():
            springs, conditions = line.strip().split(' ')

            conditions = [int(num) for num in conditions.split(',')]

            # IDEAS
            # => Solve the 'obvious' cases: extremities with a number of '?' that can only be '#' or '.'
            # Tree traversal with ? becoming . or # (0 or 1) and a function checking at every step if it is right (if not, kill the branch)
            # Each chunk has a predetermined size: n + 1 if extremity or n + 2 if middle -> divide how many '?' are available for each chunk?
            # Use sliding chunk to assess where it could go?
            # Remove the parts of the springs that have already been solved -> extremities terminated or started with a '.' -> repeat until no more solved extremities
            
            spring_fields.append((springs, conditions))

        print(spring_fields)