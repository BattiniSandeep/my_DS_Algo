# This program is to find the Largest element in an array of integers

# This function returns the index of the largest number in the array.
# Time complexity is Theta(N), where is N is the number of elements in array
def find_Largest(arr):

    # intializing 'result_index' to 0(zero)
    result_index = 0

    # Traversing the array
    for i in range(1, len(arr)):

        
        if arr[i] > arr[result_index]:
            result_index = i

    # returning reult_index
    return result_index

#lets try with an array
my_arr = [1,2,3,4,8,4,20]

# This should print 6, as the largest number is 20 and its index is 6
print(find_Largest(my_arr))
