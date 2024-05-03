def bubble_sort(sortable_items):
    """
    Implementation of a bubble sort.
    Input: sortable_items, a list of sortable items
    Output: sortable_items, the list sorted
    """
    n = len(sortable_items)

    while True:
        swapped = False
        for i in range(1, n):
            if sortable_items[i-1] > sortable_items[i]:
                # Swap the elements
                sortable_items[i - 1], sortable_items[i] = sortable_items[i], sortable_items[i - 1]
                swapped = True
        n -= 1
        if not swapped:
            break

    return sortable_items


if __name__ == '__main__':
    numbers = [7, 3, 1, 10, 6, 16, 27, 45, 0, -5, -10]
    print('Before sorting:', numbers)
    bubble_sort(numbers)
    print('After sorting:', numbers)
