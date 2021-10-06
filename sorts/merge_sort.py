def merge_sort(seq: list) -> list:
    compares = 0
    length = len(seq)
    if length > 1:
        mid = length // 2
        seq_1, seq_2 = seq[:mid], seq[mid:]
        compares += merge_sort(seq_1)
        compares += merge_sort(seq_2)
        compares += merge(seq_1, seq_2, seq)
    return compares

def merge(list_1:list, list_2:list, list_3:list, compares=0) -> list:
    compare_counter = compares
    index_1 = index_2 = index_3 = 0
    lst_1_len, lst_2_len = len(list_1), len(list_2)

    while index_1 < lst_1_len and index_2 < lst_2_len:
        compare_counter += 1
        if list_1[index_1] < list_2[index_2]:
            list_3[index_3] = list_1[index_1]
            index_1 = index_1 + 1
        else:
            list_3[index_3] = list_2[index_2]
            index_2 = index_2 + 1
            index_3 = index_3 + 1

    while index_1 < len(list_1):
        compare_counter += 1
        list_3[index_3] = list_1[index_1]
        index_1 = index_1 + 1
        index_3 = index_3 + 1

    while index_2 < len(list_2):
        compare_counter += 1
        list_3[index_3] = list_2[index_2]
        index_2 = index_2 + 1
        index_3 = index_3 + 1

    return compare_counter + 3

