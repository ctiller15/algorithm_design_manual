def insertion_sort(arr):
    arr_len = len(arr)

    for i in range(arr_len):

        j = i
        while(j > 0 and arr[j] < arr[j - 1]):
            # If this current element is larger than the previous element
            # Swap the two elements.
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp

            # Keep working backwards.
            j -= 1

    return arr
