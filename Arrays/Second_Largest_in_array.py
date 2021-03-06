# This program is to find the Second Largest element in an array of integers

# This function returns the index of the second largest number in the array.
# Time complexity is Theta(N), where is N is the number of elements in array
def find_second_largest(arr):

    # Here we initialize 'result_index' as -1 because there might be a case where the second largest element is not there.
    # for eg: arr: [55, 55, 55, 55, 55]. In this case our function should return -1.
    result_index = -1
    largest = 0
    for i in range(1, len(arr)):
        # case 1: if the element is greater than the current largest,
        # then we change current largest to second largest and update the largest element
        if arr[i] > arr[largest]:
            result_index = largest
            largest = i
        
        # case2: If the elemnet is equal, we'll ignore it.
        elif arr[i] != arr[largest]:

            # case 3: If the element is greater than the second highest and lesser than Largest element
            # Then we'll update the 'result_index' to 'i'
            if result_index == -1 or arr[i] > arr[result_index]:
                result_index = i
        
    return result_index

arr = [3,1,5,2]

# This should print 0(zero) as the second element is '3' which is at index 0(zero)
print(find_second_largest(arr))
