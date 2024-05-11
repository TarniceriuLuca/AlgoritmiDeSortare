def countingSort(list):
    max = list[0]
    for elements in list:
        if elements > max:
            max = elements

    resList = [0] * (max+1)
    for elements in list:
        resList[elements] += 1
    

    list.clear()
    for index in range(len(resList)):
        while resList[index] != 0:
            list.append(index)
            resList[index] -= 1