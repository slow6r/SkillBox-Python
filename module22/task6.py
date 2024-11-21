def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    less = [x for x in array[:-1] if x <= pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array[:-1] if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)

if __name__ == "__main__":
    numbers = [4, 9, 2, 7, 5]
    print(quick_sort(numbers))  # Ответ: [2, 4, 5, 7, 9]
