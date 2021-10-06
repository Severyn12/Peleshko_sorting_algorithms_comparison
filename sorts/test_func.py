import time
from random import randint
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from merge_sort import merge_sort
from selection_sort import selection_sort

start = time.time()
function_lst = [insertion_sort, shell_sort, merge_sort, selection_sort]
sizes = [2 ** i for i in range(7, 16)]


def create_array(size, descend=False, ascend=False, repeats=False, max_num=1000000):
    array = []
    for j in range(0, size):
        if repeats:
            array.append(randint(1, 3))
        else:
            array.append(randint(1, max_num))
    if descend:
        array.sort(reverse=True)
    elif ascend:
        array.sort()
    return array


def get_test_data(size, ordering=''):

    array_lst = []
    if ordering == 'random':
        for i in range(5):
            array = create_array(size)
            array_lst.append(array)
    elif ordering == 'descend':
        array = create_array(size, True)
        array_lst.append(array)
    elif ordering == 'ascend':
        array = create_array(size, ascend=True)
        array_lst.append(array)
    elif ordering == 'repeat':
        for i in range(3):
            array = create_array(size,repeats=True)
            array_lst.append(array)
    return array_lst


def random_arr_test(order=''):

    global function_lst, sizes
    time_complexity = []
    for size in sizes:
        temp_arr_2 = []
        arrays = get_test_data(size, order)
        for func in function_lst:
            compares = 0
            temp_arr = []
            for array in arrays:
                start = time.time()
                compares += func(array.copy())
                temp_arr.append(time.time() - start)
                if order in ('random', 'repeat'):
                    data = (sum(temp_arr) / len(temp_arr), compares//5)
                else:
                    data = (temp_arr[0], compares)
            temp_arr_2.append((data, func.__name__))
        time_complexity.append((temp_arr_2, size))
    return time_complexity


if __name__ == '__main__':
    print('Experiment №1 (randomly created array)')
    print(random_arr_test('random'))

    print('Experiment №2 (array is already sorted in ascending order)')
    print(random_arr_test('ascend'))

    print('Experiment №3 (array is already sorted in descending order)')
    print(random_arr_test('descend'))

    print('Experiment №4 (array consist of {1,2,3}, which repeat)')
    print(random_arr_test('repeat'))




