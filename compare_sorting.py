import time
import random

# Heapsort implementation
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heapsort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Quicksort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Mergesort implementation
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Compare sorting algorithms
def compare_sorting():
    sizes = [1000, 2000, 4000, 8000]
    results = {'Heapsort': [], 'Quicksort': [], 'Mergesort': []}

    print(f"{'Input Size':>10} | {'Heapsort (s)':>15} | {'Quicksort (s)':>15} | {'Mergesort (s)':>15}")
    print("-" * 62)

    for size in sizes:
        data = random.sample(range(size * 10), size)

        times = {}
        for algo, func in [('Heapsort', heapsort), ('Quicksort', quicksort), ('Mergesort', mergesort)]:
            data_copy = data[:]
            start = time.time()
            func(data_copy)
            end = time.time()
            duration = round(end - start, 6)
            results[algo].append(duration)
            times[algo] = duration

        print(f"{size:>10} | {times['Heapsort']:>15} | {times['Quicksort']:>15} | {times['Mergesort']:>15}")

if __name__ == "__main__":
    compare_sorting()
