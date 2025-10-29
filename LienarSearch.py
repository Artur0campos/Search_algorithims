import time
from random import choice


def LinearSearch(array ,num_searched):
    start = time.perf_counter()
    for element in array:
        if element == num_searched:
            end = time.perf_counter()
            totalTime = end - start
            return True, totalTime
    end = time.perf_counter()
    totalTime = end - start
    return False, totalTime
    
        
sizes = [10, 100, 1000, 10000, 100000]
for item in sizes:
    array = list(range(item))
    num = choice(array)
    found, seconds = LinearSearch(array, num)
    print(f"Tamanho: {item:6} | Tempo: {seconds:.7f} segundos")