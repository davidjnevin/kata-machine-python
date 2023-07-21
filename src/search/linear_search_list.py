def linear_search(myList, target):
    for i in range(len(myList)):
        if myList[i] == target:
            return True
    return False
