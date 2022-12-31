
class Item:
    def __init__(self, value_init):
        self.value_init = value_init
        self.list_modulo = [int(value_init)]
        self.list_operation = [None]

    def modulo(self, operation, div):
        modulo = 0

        if '*' in operation: 
            num = operation.split('*')[-1].strip()
            self.list_operation.append('*')
            num = int(num) if num.isdigit() else None
            self.list_modulo.append(num)

            if num != None:
                if num % div == 0:
                    return 0
            
        elif '+' in operation:
            num = operation.split('+')[-1].strip()
            self.list_operation.append('+')
            num = int(num) if num.isdigit() else None
            self.list_modulo.append(num)
        
        for value, op in zip(self.list_modulo, self.list_operation):
            if value == None:
                if op == '*': 
                    modulo *= modulo % div
            else:  
                if op == '*':
                    modulo *= value % div
                elif op == '+': 
                    modulo += value % div
                else:
                    modulo = value % div

        return modulo % div

class Monkey:
    def __init__(self):
        self.items_list = []
        self.operation = ''
        self.monkey_true = None
        self.monkey_false = None
        self.test_div = 1
        self.inspected = 0

    def inspect(self):
        self.inspected = self.inspected + 1

        if self.items_list[0].modulo(self.operation, self.test_div) == 0:
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
            monkeys_list[-1].items_list = [Item(x.strip()) for x in line.split(':')[-1].split(',')]

        elif 'Operation' in line:
            monkeys_list[-1].operation = line.split('=')[-1].strip()

        
        elif 'Test' in line:
            monkeys_list[-1].test_div = int(line.split('by')[-1].strip())
        
        elif 'true' in line:
            monkeys_list[-1].monkey_true = int(line.split('monkey')[-1].strip())

        elif 'false' in line:
            monkeys_list[-1].monkey_false = int(line.split('monkey')[-1].strip())

rounds = 10000

for i in range(rounds):  
    print(i)
    for monkey in monkeys_list:
        for _ in range(len(monkey.items_list)):
            if monkey.inspect():
                monkey.throw(monkeys_list[monkey.monkey_true])
            else:
                monkey.throw(monkeys_list[monkey.monkey_false])

inspection_list = sorted([m.inspected for m in monkeys_list])

for monkey in monkeys_list:
    print(monkey.inspected)
print(inspection_list[-1]*inspection_list[-2])
