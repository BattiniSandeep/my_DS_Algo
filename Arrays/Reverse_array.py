# Python program for Reversing an Array

# Time complexity - O(N), Space complexity - 0


def Rev_arr(arr):

    # Initializing low to first index of array i.e, 0
    low = 0
    # Initializing high to last index of 
    high = len(arr) -1

    # This loop approximately runs for N/2 times
    # Where N is number of elements in an array

    # Checking whether low pointer has crossed high poiter or not.
    # If crossed then loop breaks
    while low < high:

        # Swapping numbers
        arr[low], arr[high] = arr[high], arr[low]

        # Increasing low value by 1
        low += 1

        # Decreasing low value by 1
        high -= 1
    return arr

# initializing an array 
my_arr = [1,2,3,4,5]

# Output should be [5,4,3,2,1]
print(Rev_arr(my_arr))