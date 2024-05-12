import bubbleSorts as b
import bucketSorts as bk
import countingSorts as c
import insertionSorts as i
import mergeSorts as m
import quickSorts as q
import radixSorts as r
import SelectionSorts as s
import miscFunctions as f

import time as t
import math 

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()


fileName = "input100k" + ".txt"


list = []
list = f.readFile(list, fileName)
start = t.time()

#funcția de sortare:
m.quickMergeSort_sqrt(list, 0, len(list)-1)

end = t.time()
totalTime = end-start
print("sort time:", str(totalTime))
if not f.isSorted(list):
    print(f"{Fore.RED}False{Style.RESET_ALL}")
else:
    print(f"{Fore.GREEN}True{Style.RESET_ALL}")

with open("result.txt", "w") as w:
    w.write(str(list))
