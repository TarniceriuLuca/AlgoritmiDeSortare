#@article{horsmalahti2012comparison,
#  title={Comparison of bucket sort and radix sort},
#  author={Horsmalahti, Panu},
#  journal={arXiv preprint arXiv:1206.3511},
#  year={2012}
#}



import SelectionSorts as s
import mergeSorts as m

def selectionBucket(list, n):
    # n is the number of buckets
    resList = []
    for i in range(n):
        resList.append([])
    max = list[0]
    for elements in list:
        if elements > max:
            max = elements


    for elements in list:
        resList[(n-1)*elements//max].append(elements)

    for buckets in resList:
        s.OGselection(buckets)
    
    list.clear()
    for i in range(10):
        list.extend(resList[i])

def mergeBucket(list, n):
    # n is the number of buckets
    resList = []
    for i in range(n):
        resList.append([])
    max = list[0]
    for elements in list:
        if elements > max:
            max = elements


    for elements in list:
        resList[(n-1)*elements//max].append(elements)

    for buckets in resList:
        m.OGmergeSort(buckets, 0, len(buckets)-1)
    
    list.clear()
    for i in range(10):
        list.extend(resList[i])

def quickMergeBucket(list, n):
     # n is the number of buckets
    resList = []
    for i in range(n):
        resList.append([])
    max = list[0]
    for elements in list:
        if elements > max:
            max = elements


    for elements in list:
        resList[(n-1)*elements//max].append(elements)

    for buckets in resList:
        m.quickMergeSort_sqrt(buckets, 0, len(buckets)-1)
    
    list.clear()
    for i in range(10):
        list.extend(resList[i])




def bucketBucket(list, result, n):
    # recursion depth limit
    bucketList = []
    for _ in range(n):
        bucketList.append([])
    max = list[0]
    for elements in list:
        if elements > max:
            max = elements


    for elements in list:
        bucketList[(n-1)*elements//max].append(elements)

    for buckets in bucketList:
        if len(buckets) > 1:
            bucketBucket(buckets, result, 10)
        else:
            result.extend(bucketList[0])

