#@article{dutta2013approach,
#  title={An approach to improve the performance of insertion sort algorithm},
#  author={Dutta, Partha Sarathi},
#  journal={International Journal of Computer Science \& Engineering Technology (IJCSET)},
#  volume={4},
#  number={05},
#  pages={503--505},
#  year={2013}
#}

def OGinsertion(list):
    for i in range(1, len(list)):
        j = i-1
        v = list[i]
        while j >= 0 and list[j] > v:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = v


def improvedInsertion(list):
    #passes through the list once, and compares i, n-i; then normal insertion;
    for i in range(len(list)//2):
        if(list[i] > list[len(list)-i -1]):
            (list[i], list[len(list)-i -1]) = (list[len(list)-i -1], list[i])
    OGinsertion(list)
