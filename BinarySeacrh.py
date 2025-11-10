import time
from random import choice


def binarySearch(array,num_searched):

    start_seconds = time.perf_counter()
    start = 0
    end = len(array) - 1

    while start <= end:
        pointer = (end + start)//2
        if pointer == num_searched:
            end_seconds = time.perf_counter()
            total_seconds = end_seconds - start_seconds
            return True, total_seconds
        
        elif pointer < num_searched:
            end = pointer - 1

        else:
            start = pointer + 1

    end_seconds = time.perf_counter()
    total_seconds = end_seconds - start_seconds
    return -1, total_seconds


sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000000]
for item in sizes:
    array = list(range(item))
    num = choice(array)
    found, seconds = binarySearch(array, num)
    print(f"Tamanho: {item:6} | Tempo: {seconds:.7f} segundos")