class Monkey:
    def __init__(self):
        self.items_list = []
        self.operation_type = ''
        self.operation_num = None
        self.monkey_true = None
        self.monkey_false = None
        self.test_div = 1
        self.inspected = 0

    def inspect(self):
        self.inspected = self.inspected + 1
        num = self.items_list[0] if self.operation_num == None else self.operation_num

        if self.operation_type == '+':
            self.items_list[0] += num

        elif self.operation_type == '*':
            self.items_list[0] *= num

    def test(self):
        self.items_list[0] = self.items_list[0]//3
        if self.items_list[0] % self.test_div == 0:
            return True
        else:
            return False

    def throw(self, receiver):
        receiver.items_list.append(self.items_list.pop(0))

with open('input_11') as data:
    monkeys_list = []

    for line in data.readlines():
        if 'Monkey' in line:
            monkeys_list.append(Monkey())
        
        elif 'Starting items' in line:
            monkeys_list[-1].items_list = [int(x) for x in line.split(':')[-1].split(',')]

        elif 'Operation' in line:
            if '+' in line:
                monkeys_list[-1].operation_type = '+'
            elif '*' in line:
                monkeys_list[-1].operation_type = '*'
            digit = line.split(monkeys_list[-1].operation_type)[-1].strip()
            if digit.isdigit():
                monkeys_list[-1].operation_num = int(digit)
        
        elif 'Test' in line:
            monkeys_list[-1].test_div = int(line.split('by')[-1].strip())
        
        elif 'true' in line:
            monkeys_list[-1].monkey_true = int(line.split('monkey')[-1].strip())

        elif 'false' in line:
            monkeys_list[-1].monkey_false = int(line.split('monkey')[-1].strip())

rounds = 20

for i in range(rounds):  
    for monkey in monkeys_list:
        for _ in range(len(monkey.items_list)):
            monkey.inspect()

            if monkey.test():
                monkey.throw(monkeys_list[monkey.monkey_true])
            else:
                monkey.throw(monkeys_list[monkey.monkey_false])

inspection_list = sorted([m.inspected for m in monkeys_list])

print(inspection_list[-1]*inspection_list[-2])