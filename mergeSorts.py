
#@article{article,
#author = {Mishal, Ibtehal and Alkhatibe, Rasha and Hiasat, Razan},
#year = {2021},
#month = {10},
#pages = {975-8887},
#title = {Comparative Study of Two Divide and Conquer Sorting Algorithms: Modified Quick Sort and Merge Sort},
#volume = {183},
#journal = {International Journal of Computer Applications},
#doi = {10.5120/ijca2021921702}
#}


#@inproceedings{cheema2016contrastive,
#  title={Contrastive analysis of bubble \& merge sort proposing hybrid approach},
#  author={Cheema, Sehrish Munawar and Sarwar, Nadeem and Yousaf, Fatima},
#  booktitle={2016 Sixth International Conference on Innovative Computing Technology (INTECH)},
#  pages={371--375},
#  year={2016},
#  organization={IEEE}
#}

from quickSorts import QuickSort2Pivot as quicksort
import math

def merge(list, start, mid, end):
    n1 = mid-start+1
    n2 = end-mid
    L = []
    R = []
    for i in range(n1):
        L.append(list[start + i])
    for j in range(n2):
        R.append(list[mid+1 + j])



    i = 0
    j = 0
    k = start

    while i<n1 and j<n2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i+=1
        else:
            list[k] = R[j]
            j+=1
        k+=1

    while i < n1:
        list[k] = L[i]
        i+=1
        k+=1
    while j < n2:
        list[k] = R[j]
        j+=1
        k+=1


def OGmergeSort(list, start, end):
    if start < end:
        mid = (start + end)//2
        OGmergeSort(list, start, mid)
        OGmergeSort(list, mid+1, end)
        merge(list, start, mid, end)


def bubbleMergeSort(list, start, end):
    if end-start > 10:
        mid = (start + end)//2
        bubbleMergeSort(list, start, mid)
        bubbleMergeSort(list, mid+1, end)
        merge(list, start, mid, end)

    sorted = False
    n = end-start+1

    i = start;
    while i < n//2 and not sorted:
        sorted = True
        for j in range(i, (end+1)-(i+1)):
            if list[j] > list[j+1]:
                (list[j], list[j+1]) = (list[j+1], list[j])
                sorted = False
            if list[(end+1)-(j+1)] < list[(end+1)-(j+2)]:
                (list[(end+1)-(j+1)], list[n-(j+2)]) = (list[(end+1)-(j+2)], list[(end+1)-(j+1)])
                sorted = False  
        i+=1  


def quickMergeSort_log(list, start, end):
    if end - start > math.log2(len(list)):
        mid = (start + end)//2
        quickMergeSort_log(list, start, mid)
        quickMergeSort_log(list, mid+1, end)
        merge(list, start, mid, end)
    else:
        list[start:end+1] = quicksort(list[start:end+1])



def quickMergeSort_sqrt(list, start, end):
    if end - start > math.sqrt(len(list)):
        mid = (start + end)//2
        quickMergeSort_sqrt(list, start, mid)
        quickMergeSort_sqrt(list, mid+1, end)
        merge(list, start, mid, end)
    else:
        list[start:end+1] = quicksort(list[start:end+1])
