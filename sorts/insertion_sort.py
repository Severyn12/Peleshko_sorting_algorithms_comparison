def insertion_sort(sequence):
    length = len(sequence) - 1
    compare_counter = 0
    for i in range(1, length):
        k = i-1
        current_element = sequence[i]
        compare_counter += 1
        while (sequence[k] > current_element) and (k >= 0):
            compare_counter += 1
            sequence[k+1] = sequence[k]
            k -= 1
        sequence[k+1] = current_element
    return compare_counter