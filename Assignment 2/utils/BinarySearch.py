# Binary Search in Python
# Works only on a sorted list
# Idea: Repeatedly divide the search range in half until the target is found.
def binary_search(arr, target):
    print(f"Searching for {target} in {arr}")
    left = 0
    right = len(arr) - 1
    step = 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: Checking middle index {mid} -> {arr[mid]}")
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"{target} is greater than {arr[mid]}, so search right half.")
            left = mid + 1
        else:
            print(f"{target} is smaller than {arr[mid]}, so search left half.")
            right = mid - 1
            step += 1
            print(f"{target} was not found in the list.")
            return -1

# Example usage
#numbers = [11, 15, 23, 45, 70, 80, 99] # Sorted list
# Searching for a number that exists
#binary_search(numbers, 70)
#print("\n---\n")
# Searching for a number that does not exist
#binary_search(numbers, 50)