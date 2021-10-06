def selection_sort(seq: list) -> list:
    compare_counter = 0
    length = len(seq) - 1
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            current_element = seq[j]
            compare_counter += 1
            if current_element <= seq[min_index]:
                min_index = j
        seq[min_index], seq[i] = seq[i], seq[min_index]
    return compare_counter

