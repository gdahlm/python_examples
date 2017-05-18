"""Basic sort function examples"""
def bubble_sort(array):
    """bubble_sort(list) -> list

    >>> bubble_sort([3, 2, 13, 4, 6, 5, 7, 8, 1, 20])
    [1, 2, 3, 4, 5, 6, 7, 8, 13, 20]
    """
    for value in range(len(array) - 1, 0, -1):
        for key in range(value):
            if array[key] > array[key + 1]:
                tempval = array[key]
                array[key] = array[key + 1]
                array[key + 1] = tempval
    return array


def selection_sort(array):
    """selection_sort(list) -> list

    >>> selection_sort([3, 2, 13, 4, 6, 5, 7, 8, 1, 20])
    [1, 2, 3, 4, 5, 6, 7, 8, 13, 20]
    """
    for slot in range(len(array) - 1, 0, -1):
        max_sofar = 0
        for pos in range(1, slot + 1):
            if array[pos] > array[max_sofar]:
                max_sofar = pos

        tempval = array[slot]
        array[slot] = array[max_sofar]
        array[max_sofar] = tempval
    return array


def insertion_sort(array):
    """insertion_sort(list) -> list

    >>> insertion_sort([3, 2, 13, 4, 6, 5, 7, 8, 1, 20])
    [1, 2, 3, 4, 5, 6, 7, 8, 13, 20]
    """
    for index in range(1, len(array)):
        value_now = array[index]
        pos = index
        while pos > 0 and array[pos - 1] > value_now:
            array[pos] = array[pos - 1]
            pos = pos - 1
        array[pos] = value_now
    return array


def shell_sort(array):
    """shell_sort(list) -> list

    >>> shell_sort([3, 2, 13, 4, 6, 5, 7, 8, 1, 20])
    [1, 2, 3, 4, 5, 6, 7, 8, 13, 20]
    """
    sub_count = len(array) / 2
    while sub_count > 0:
        for start in range(sub_count):
            gap_insertion_sort(array, start, sub_count)
        sub_count = sub_count / 2
    return array


def gap_insertion_sort(array, start, gap):
    for index in range(start + gap, len(array), gap):
        """Helper for shell_sort"""
        value_now = array[index]
        pos = index
        while pos >= gap and array[pos - gap] > value_now:
            array[pos] = array[pos - gap]
            pos = pos - gap
        array[pos] = value_now
    return array


def merge_sort(array):
    """merge_sort(list) - list

    Recursive divide and conquer

    >>> merge_sort([3, 2, 13, 4, 6, 5, 7, 8, 1, 20])
    [1, 2, 3, 4, 5, 6, 7, 8, 13, 20]
    """
    if len(array) > 1:
        mid = len(array) / 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i, k, j = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1
    return array


def quick_sort(array):
    """quick_sort(list) -> list

    >>> quick_sort([2, 5, 4, 6, 7, 3, 1, 4, 12, 11])
    [2, 5, 4, 6, 7, 3, 1, 4, 12, 11]
    """
    quick_sort_help(array, 0, len(array) - 1)
    return foo


def quick_sort_help(array, first, last):
    """helper for quick_sort"""
    if first < last:
        split_point = partition(array, first, last)
        quick_sort_help(array, first, split_point - 1)
        quick_sort_help(array, split_point + 1, last)


def partition(array, first, last):
    """helper for quick_sort"""
    pivot_value = array[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp

    temp = array[first]
    array[first] = array[right_mark]
    array[right_mark] = temp
    return right_mark
