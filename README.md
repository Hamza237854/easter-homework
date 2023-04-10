# easter-homework

______________
< happy easter >
 --------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

0) Generare numeri interi pseudocasuali in Python è molto semplice:
      import random
      random.randint(a, b) #genera un intero casuale nell'intervallo [a, b]
   Costruire una lista contenente 1000 numeri casuali compresi tra -200 e 200,
   utilizzando la list comprehension.

1) Implementare l'algoritmo Insertion Sort e utilizzarlo per ordinare la lista
   costruita al punto 0.

2) Misurare il tempo di esecuzione di un frammento di codice in Python è semplice:
      import time
      start_time = time.time()
      #code...
      end_time = time.time()
      print(end_time - start_time)

   Confrontare il tempo di esecuzione della vostra implementazione di Insertion Sort
   con il tempo di esecuzione del metodo sort() built-in di Python, sulla lista
   costruita al punto 0.

3) Implementare l'algoritmo Merge Sort, partendo dalla procedura 'merge' vista in classe.
   Studiarne il funzionamento qui: https://en.wikipedia.org/wiki/Merge_sort

4) Confrontare il tempo di esecuzione della vostra implementazione di Merge Sort
   con il tempo di esecuzione del metodo sort() built-in di Python, sulla lista
   costruita al punto 0.

5) Implementare gli algoritmi Bubble Sort e Selection Sort.

6) Utilizzare un dizionario per contare il numero di occorrenze di un intero k compreso
   nell'intervallo [0, 10] in una tupla tp di interi, tutti appartenenti all'intervallo
   [0, 10].
   Inizializzare il dizionario in questo modo, utilizzando la list comprehension:
       {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
   la singola coppia (key:value) indica che il numero 'key' compare 'value' volte nella
   lista.

7) Implementare il Cifrario di Vigenère, lavorando soltanto sulle lettere minuscole
   dell'alfabeto inglese.
   Studiare il funzionamento del cifrario qui: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
