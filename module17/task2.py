def merge_sorted_lists(list1, list2):
    merged = sorted(set(list1 + list2))
    return merged

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
