# In this problem we'll check whether the array is sorted or not.
# To check, we'll traverse the array from left to right till the end
# If the array[i] is smaller than the array[i-1] then we return False
# else return True

# Time complexiy is BigO(N) where N is the size of the array

def is_sorted(arr):

    # traversing the array
    for i  in range(1, len(arr)):
        # checking whether the element of arr[i-1] is greater than the array[i] or not
        if arr[i-1] > arr[i]:
            # if greater, we'll return False
            return False
        
    # After Traversing the array if there is no element whuch satisfies the above condition
    # then we'll return True
    return True

arr = [1,2,3,4,5,6,10,8,9]

# this should print True as the given array is sorted
print(is_sorted(arr))