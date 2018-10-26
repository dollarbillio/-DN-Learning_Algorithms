# Divide and Conquer
def binarysearch(list_1, result):
    mid = len(list_1) // 2

    if len(list_1) == 1:
        if list_1[mid] == result:
            return "There is Found"
        else:
            return "There is None" 
    else: 
        if list_1[mid] > result:
            return binarysearch(list_1[:mid], result)
        elif list_1[mid] <= result:
            return binarysearch(list_1[mid:], result)
