def bubble_sort_recursive(A, n=None):
    if n is None:
        n = len(A)

    if n == 1:
        return

    # Perform one pass of Bubble Sort
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]

    # Recur for the remaining unsorted part of the array
    bubble_sort_recursive(A, n - 1)


def selection_sort_recursive(A, n=None, index=0):
    if n is None:
        n = len(A)

    if index == n:
        return

    # Find the minimum element in the remaining unsorted array
    min_index = index
    for i in range(index + 1, n):
        if A[i] < A[min_index]:
            min_index = i

    # Swap the found minimum element with the element at index
    A[index], A[min_index] = A[min_index], A[index]

    # Recur for the remaining unsorted array
    selection_sort_recursive(A, n, index + 1)


def insertion_sort_recursive(A, n=None):
    if n is None:
        n = len(A)

    if n <= 1:
        return

    # Recur to sort the first n-1 elements
    insertion_sort_recursive(A, n - 1)

    # Insert the nth element into its correct position
    last = A[n - 1]
    j = n - 2

    # Shift elements of the sorted part to the right to make space for the nth element
    while j >= 0 and A[j] > last:
        A[j + 1] = A[j]
        j -= 1

    A[j + 1] = last


def user_interface():

    # Get the array input from the user
    array_input = input("Enter the array of integers, separated by spaces: ")
    A = list(map(int, array_input.split()))

    # Provide algorithm choices
    print("\nSelect the sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")

    choice = input("\nEnter your choice (1/2/3): ")

    # Sort the array based on the user's choice
    if choice == '1':
        bubble_sort_recursive(A)
        print("\nSorted array using Bubble Sort:", A)
    elif choice == '2':
        selection_sort_recursive(A)
        print("\nSorted array using Selection Sort:", A)
    elif choice == '3':
        insertion_sort_recursive(A)
        print("\nSorted array using Insertion Sort:", A)
    else:
        print("\nInvalid choice. Please run the program again and select a valid option.")


# Run the user interface
if __name__ == "__main__":
    user_interface()
