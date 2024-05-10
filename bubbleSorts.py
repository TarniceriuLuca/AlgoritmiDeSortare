#@inproceedings{min2010analysis,
#  title={Analysis on bubble sort algorithm optimization},
#  author={Min, Wang},
#  booktitle={2010 International forum on information technology and applications},
#  volume={1},
#  pages={208--211},
#  year={2010},
#  organization={IEEE}
#}


#@article{friend1956sorting,
#  title={Sorting on electronic computer systems},
#  author={Friend, Edward H},
#  journal={Journal of the ACM (JACM)},
#  volume={3},
#  number={3},
#  pages={134--168},
#  year={1956},
#  publisher={ACM New York, NY, USA}
#}

import time as t

def OGbubble(list):
    sorted = False

    while not sorted:
        sorted = True

        for i in range(1, len(list)):
            if list[i] < list[i-1]:
                sorted = False
                (list[i], list[i-1]) = (list[i-1], list[i])


def improvedBubble(list):
    sorted = False

    for i in range(1, len(list)):
        sorted = True
        for j in range(1, len(list)-(i-1)): #la fiecare pas ultimele i elemente sunt sortate, astfel nu este necesar sa fie comparate
            if list[j] < list[j-1]:
                sorted = False
                (list[j], list[j-1]) = (list[j-1], list[j])
        if sorted == True:
            break


def doubleBubble(list):
    sorted = False
    n = len(list)

    i = 0;
    while i < n//2 and not sorted:
        sorted = True
        for j in range(i, n-(i+1)):
            if list[j] > list[j+1]:
                (list[j], list[j+1]) = (list[j+1], list[j])
                sorted = False
            if list[n-(j+1)] < list[n-(j+2)]:
                (list[n-(j+1)], list[n-(j+2)]) = (list[n-(j+2)], list[n-(j+1)])
                sorted = False  
        i+=1    
