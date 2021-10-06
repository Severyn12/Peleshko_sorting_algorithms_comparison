def shell_sort(seq):
    length = len(seq)
    separator = 1
    compare_counter = 0
    while separator < length:
        separator = 3 * separator + 1
    while separator > 0:
        for i in range(separator, length):
            j = i
            compare_counter += 1
            while (seq[j] < seq[j-separator]) and (j >= separator):
                compare_counter += 1
                key = seq[j-separator]
                seq[j-separator] = seq[j]
                seq[j] = key
                j -= separator
        separator = int(separator - separator/3)

    return compare_counter

