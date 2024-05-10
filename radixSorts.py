# Harold H. Steward

#@article{horsmalahti2012comparison,
#  title={Comparison of bucket sort and radix sort},
#  author={Horsmalahti, Panu},
#  journal={arXiv preprint arXiv:1206.3511},
#  year={2012}
#}

def pseudoBucketSort(list, digit):
    resList = []
    for i in range(10):
        resList.append([])
    
    for elements in list:
        resList[elements//digit%10].append(elements)
    
    list.clear()
    for i in range(10):
        list.extend(resList[i])

    return list





def radix(list):
    max = list[0]
    digit = 1
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]

    while max != 0:
        max //= 10
        list = pseudoBucketSort(list, digit)
        digit*=10
        


