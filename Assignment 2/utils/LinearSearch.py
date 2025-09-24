# Linear Search in Python
# Linear search means we go through the list one by one
# until we find the target element or reach the end.
def linear_search(arr, target):
    print(f"Searching for {target} in {arr}")
    # Go through the list element by element
    for index in range(len(arr)):
        print(f"Step {index + 1}: Checking element at index {index} -> {arr[index]}")
    #    If the current element matches the target, return its position
        if arr[index] == target:
            print(f"Found {target} at index {index}")
            return index
    # If loop finishes without finding the target
    print(f"{target} was not found in the list.")
    return -1
    
    # Example usage
    #numbers = [10, 23, 45, 70, 11, 15]
    # Try searching for a number that exists
    #linear_search(numbers, 70)
    #print("\n---\n")
    # Try searching for a number that does not exist
    #linear_search(numbers, 99)