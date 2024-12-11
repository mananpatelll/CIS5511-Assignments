# %%
import random
import time

insertion_calls = 0
merge_sort_merge_calls = 0


def insertion_sort(arr):
    global insertion_calls
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            insertion_calls += 1  # count each while loop
        arr[j + 1] = key

# Global variable to count each merge function call


def merge(arr, p, q, r):
    global merge_sort_merge_calls

    nL = q - p + 1
    nR = r - q
    left = arr[p:p + nL]
    right = arr[q + 1:q + 1 + nR]

    merge_sort_merge_calls += 1  # Count each merge function call

    i = 0
    j = 0
    k = p
    while i < nL and j < nR:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < nL:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < nR:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


def reset_counters():
    global insertion_calls, merge_sort_merge_calls
    insertion_calls = 0
    merge_sort_merge_calls = 0


def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]


def main():
    test_sizes = [10, 100, 1000]
    num_tests = 5

    for size in test_sizes:  # For each size in test_size
        print(f"Array Size: {size}")
        for i in range(num_tests):  # Repeat test 5 times for each size
            arr1 = generate_random_array(size)  # To generate random array
            arr2 = arr1.copy()  # Clone the array for fair comparison

            # Perform Insertion Sort with timer
            reset_counters()  # Reset counters before each algorithm
            start_time = time.perf_counter()  # Start counter
            insertion_sort(arr1)
            end_time = time.perf_counter()  # Stop counter
            insertion_sort_time = (end_time - start_time) * \
                1e9  # Convert to nanoseconds

            # Perform Merge Sort with timer
           # reset_counters()  # Reset counters before each algorithm
            start_time = time.perf_counter()
            merge_sort(arr2, 0, len(arr2) - 1)
            end_time = time.perf_counter()
            merge_sort_time = (end_time - start_time) * \
                1e9  # Convert to nanoseconds

            # Display results and counters
            print(f"Test {i + 1}:")
            print(f"Insertion Sort Time (ns): {insertion_sort_time:.2f}")
            print(f"Insertion Sort Calls: {insertion_calls}")
            print(f"Merge Sort Time (ns): {merge_sort_time:.2f}")
            print(f"Merge Sort Merge Calls: {merge_sort_merge_calls}")
            print()


if __name__ == "__main__":
    main()
