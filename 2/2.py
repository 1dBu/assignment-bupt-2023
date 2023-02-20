import random
import time

def generate_random_list(length):
    return [random.randint(0, 1000) for _ in range(length)]

def insertion_sort(arr):
    compare_count = 0
    move_count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            compare_count += 1
            arr[j+1] = arr[j]
            move_count += 1
            j -= 1
        compare_count += 1
        arr[j+1] = key
        move_count += 1
    return compare_count, move_count

def merge_sort(arr):
    compare_count = 0
    move_count = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        compare_left, move_left = merge_sort(left_half)
        compare_right, move_right = merge_sort(right_half)
        compare_count += compare_left + compare_right
        move_count += move_left + move_right

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            compare_count += 1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
                move_count += 1
            else:
                arr[k] = right_half[j]
                j += 1
                move_count += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            move_count += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            move_count += 1

    return compare_count, move_count

def bubble_sort(arr):
    compare_count = 0
    move_count = 0
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            compare_count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                move_count += 3
    return compare_count, move_count

def quick_sort(arr):
    compare_count = 0
    move_count = 0
    if len(arr) <= 1:
        return compare_count, move_count
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            compare_count += 1
            if arr[i] < pivot:
                left.append(arr[i])
                move_count += 1
            else:
                right.append(arr[i])
                move_count += 1
        compare_left, move_left = quick_sort(left)
        compare_right, move_right = quick_sort(right)
        compare_count += compare_left + compare_right
        move_count += move_left + move_right
        arr[:] = left + [pivot] + right
        move_count += len(arr) - 1
        return compare_count, move_count

def selection_sort(arr):
    compare_count = 0
    move_count = 0
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            compare_count += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            move_count += 3
    return compare_count, move_count

if __name__ == '__main__':
    num_of_lists = 5
    list_lengths = [100] #, 200, 300, 400, 500]
    algorithms = [insertion_sort, merge_sort, bubble_sort, quick_sort, selection_sort]
    for length in list_lengths:
        print(f"List length: {length}")
        for i in range(num_of_lists):
            print("Trial #",i)
            arr = generate_random_list(length)
            for algorithm in algorithms:
                arr_copy = arr[:]
                start_time = time.time()
                compare_count, move_count = algorithm(arr_copy)
                end_time = time.time()
                print(f"{algorithm.__name__}: {compare_count} compares, {move_count} moves, {end_time - start_time:.6f} seconds")
        print("=" * 40)
