# The basic idea of a selection sort is that you take your smallest element,
# and place it at the front.
# You repeat this until you've traversed the entire collection

def selection_sort(unsorted_list):
    list_length = len(unsorted_list)

    for i in range(list_length):
        sort_min = unsorted_list[i]
        sort_ind = i

        for j in range(i + 1, list_length):
            # Check to see if the next value is smaller than the previous value for every value.
            if unsorted_list[j] < sort_min:
                sort_min = unsorted_list[j]
                # Remember, the minimum value is only used for recording the minimum.
                # You need the value and the position to be able to swap correctly.
                sort_ind = j
            # If it is, record it.

        # After you've gone through every value, swap the smallest element with the first element.
        temp = unsorted_list[i]
        unsorted_list[i] = sort_min
        unsorted_list[sort_ind] = temp

    return unsorted_list
