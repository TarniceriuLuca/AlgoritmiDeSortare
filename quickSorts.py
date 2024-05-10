#@article{article,
#author = {Budiman, Mohammad and Zamzami, Elviawaty and Rachmawati, Dian},
#year = {2017},
#month = {03},
#pages = {012051},
#title = {Multi-Pivot Quicksort: an Experiment with Single, Dual, Triple, Quad, and Penta-Pivot Quicksort Algorithms in Python},
#volume = {180},
#journal = {IOP Conference Series: Materials Science and Engineering},
#doi = {10.1088/1757-899X/180/1/012051}
#}


#@article{hoare1962quicksort,
#  title={Quicksort},
#  author={Hoare, Charles AR},
#  journal={The computer journal},
#  volume={5},
#  number={1},
#  pages={10--16},
#  year={1962},
#  publisher={Oxford University Press}
#}
import math


def QuickSort(list):
    n = len(list)
    if n <= 1:
        return list
    elif n == 2:
        return sorted(list)
    pivot1 = list.pop(0)
    a = []
    b = []
    for element in list:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element:
            b.append(element)
    return QuickSort(a) + [pivot1] + QuickSort(b)



def QuickSort2Pivot(list):
    n = len(list)
    if n <= 1:
        return list
    elif n == 2:
        return sorted(list)
    pivot1, pivot2 = sorted([list.pop(0), list.pop(0)])
    a = []
    b = []
    c = []
    for element in list:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element < pivot2:
            b.append(element)
        else:
            c.append(element)
    return QuickSort2Pivot(a) + [pivot1] + QuickSort2Pivot(b) + [pivot2] +QuickSort2Pivot(c) 


def QuickSort3Pivot(list):
    n = len(list)
    if n <= 1:
        return list
    elif n == 2:
        return sorted(list)
    pivot1, pivot2, pivot3 = sorted([list.pop(0), list.pop(0), list.pop(0)])
    a = []
    b = []
    c = []
    d = []
    for element in list:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element < pivot2:
            b.append(element)
        elif pivot2 <= element < pivot3:
            c.append(element)
        else:
            d.append(element)
    return QuickSort3Pivot(a) + [pivot1] + QuickSort3Pivot(b) + [pivot2] +QuickSort3Pivot(c) + [pivot3] + QuickSort3Pivot(d) 
