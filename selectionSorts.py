#@article{jadoon2011design,
#  title={Design and analysis of optimized selection sort algorithm},
#  author={Jadoon, Sultanullah and Solehria, Salman Faiz and Rehman, Salim ur and Jan, Hamid},
#  journal={International Journal of Electric \& Computer Sciences (IJECS-IJENS)},
#  volume={11},
#  number={01},
#  pages={16--22},
#  year={2011},
#  publisher={Citeseer}
#}

def OGselection(list):
    currentMax = len(list)-1
    maxIndex = 0
    for _ in range(len(list)):
        for j in range(currentMax+1):
            if(list[j] > list[maxIndex]):
                maxIndex = j
        (list[currentMax], list[maxIndex]) = (list[maxIndex], list[currentMax])
        currentMax -= 1
        maxIndex = 0

def doubleSelection(list):
    
    for currentMin in range(len(list)//2+1):

        currentMax = len(list) - 1 - currentMin
        minIndex = currentMin
        maxIndex = currentMax


        for j in range(currentMin, currentMax+1):
            if(list[j] > list[maxIndex]):
                maxIndex = j
            if(list[j] < list[minIndex]):
                minIndex = j

        
        (list[currentMin], list[minIndex]) = (list[minIndex], list[currentMin])

        if(maxIndex == currentMin):
            maxIndex = minIndex

        (list[currentMax], list[maxIndex]) = (list[maxIndex], list[currentMax])
