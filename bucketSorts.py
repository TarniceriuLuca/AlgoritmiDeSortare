# Comparison of Bucket Sort and RADIX Sort

import SelectionSorts as s
import mergeSorts as m


def selectionBucket(list, nrOfBuckets):
    # n is the number of buckets
    resList = []
    for i in range(nrOfBuckets):
        resList.append([])
    max = list[0]
    for elements in list:
        if elements > max:
            max = elements


    for elements in list:
        resList[(nrOfBuckets-1)*elements//max].append(elements)

    for buckets in resList:
        s.OGselection(buckets)
    
    list.clear()
    for i in range(10):
        list.extend(resList[i])

def mergeBucket(list, nrOfBuckets):
    # n is the number of buckets
    resList = []
    for i in range(nrOfBuckets):
        resList.append([])
    max = list[0]
    for elements in list:
        if elements > max:
            max = elements


    for elements in list:
        resList[(nrOfBuckets-1)*elements//max].append(elements)

    for buckets in resList:
        m.OGmergeSort(buckets, 0, len(buckets)-1)
    
    list.clear()
    for i in range(10):
        list.extend(resList[i])

def quickMergeBucket(list, nrOfBuckets):
     # n is the number of buckets
    resList = []
    for i in range(nrOfBuckets):
        resList.append([])
    max = list[0]
    for elements in list:
        if elements > max:
            max = elements


    for elements in list:
        resList[(nrOfBuckets-1)*elements//max].append(elements)

    for buckets in resList:
        m.quickMergeSort_sqrt(buckets, 0, len(buckets)-1)
    
    list.clear()
    for i in range(10):
        list.extend(resList[i])




def bucketBucket(list, result, nrOfBuckets):
    # recursion depth limit
    bucketList = []
    for _ in range(nrOfBuckets):
        bucketList.append([])
    max = list[0]
    for elements in list:
        if elements > max:
            max = elements


    for elements in list:
        bucketList[(nrOfBuckets-1)*elements//max].append(elements)

    for buckets in bucketList:
        if len(buckets) > 1:
            bucketBucket(buckets, result, 10)
        else:
            result.extend(bucketList[0])
            
def quickBucket(list):
    # recursion depth limit
    pass
