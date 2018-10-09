def insertion_sort (item):

    for i in range (0, len(item)):
        j = i
        while j > 0 and item[j] < item [j-1]:
            n = item[j]
            # swap positions
            item[j] = item[j-1]
            item[j-1] = n
            j-= 1

    return item
