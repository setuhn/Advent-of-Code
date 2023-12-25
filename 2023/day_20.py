
import timeit
start = timeit.default_timer()


if __name__ == '__main__':



    with open(f'day_20.1-test.txt') as data:
        for line in data.readlines():
            module_type, outputs = line.strip().split(' -> ')
            outputs = [out for out in outputs.split(',')]

            print(module_type, outputs)


    print(f'Time :{timeit.default_timer() - start} s')