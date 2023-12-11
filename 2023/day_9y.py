def calculate_difference(values):
    return [values[idx+1] - values[idx] for idx, _ in enumerate(values) if idx < len(values)-1]

def generate_all_differences(values):
    differences_list = [values]

    while sum(differences_list[-1]) != 0:
        differences_list.append(calculate_difference(differences_list[-1]))

    return differences_list

def extrapolate_future(differences_list):
    extrapolation = 0

    for difference in reversed(differences_list):
        extrapolation += difference[-1]

    return extrapolation

def extrapolate_past(differences_list):
    extrapolation = 0

    for difference in reversed(differences_list):
        extrapolation = difference[0] - extrapolation

    return extrapolation


if __name__ == '__main__':

    with open(f'day_9.txt') as data:
        
        extrapolation_future_sum = 0
        extrapolation_past_sum = 0

        for history in data.readlines():
            values = [int(val) for val in history.strip().split(' ')]
            differences_list = generate_all_differences(values)
            extrapolation_future = extrapolate_future(differences_list)
            extrapolation_past = extrapolate_past(differences_list)

            extrapolation_future_sum += extrapolation_future
            extrapolation_past_sum += extrapolation_past


        print(f'Answer to part 1: {extrapolation_future_sum}')
        print(f'Answer to part 2: {extrapolation_past_sum}')

