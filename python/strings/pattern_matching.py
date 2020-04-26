def find_match(sub_str: str, search_set: str) -> str:
    """
    Searches a complete string for a given substring
    """

    # Initialize the lengths of our searchables.
    search_len = len(sub_str)
    set_len = len(search_set)

    # Begin traversing the string
    for i in range(set_len - search_len + 1):
        j = 0

        # if we haven't hit the end of the string, keep checking the next character
        # until it fails.
        while j < search_len and sub_str[j] == search_set[i + j]:
            j += 1

        if j == search_len:
            return i

    return -1
