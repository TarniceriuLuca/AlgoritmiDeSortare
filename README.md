Pentru rularea programelor, toate fișierele trebuie incluse într-un proiect, iar în fișierul "main.py"
se va introduce în atribuirea variabilei "fileName", numele fișierului care se dorește a fi sortat.

În linia următoare celei care conține comentariul:"funcția de sortare:", se va introduce funcția algoritmului care
trebuie folosit, precedat de selectorul fișierului sursă. O listă a tuturor selectorilor este găsită la începutul
programului.

Toate funțiile de sortare, cu excepția Quicksort, modifică lista trimisă ca parametru. Pentru apelarea oricărei 
funcții Quicksort, este necesară atribuirea rezultatului funcției, listei inițiale
(exemplu de apel: "list = q.QuickSort(list)").

Observație: Unele funcții de sortare necesită mai mulți parametrii. Funcțiile care au nevoie de precizarea începutului și sfârșitului listei, trebuie apelate cu parametrii "0" pentru "start", respectiv "len(list)-1" pentru "end".
(exemplu: "m.quickMergeSort_sqrt(list, 0, len(list)-1)")

După execuția programului, în terminal va fi afișat timpul de execuție, și valoarea "True" dacă lista este
întradevăr sortată, "False" în caz contrar. De asemenea va fi creat fișierul "result.txt" în care se va salva
lista sortată.
