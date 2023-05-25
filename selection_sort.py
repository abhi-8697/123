def Selection_sort(array,size):
    for i in range(size):
        min_index = i
        for j in range(i+1,size):
            if(array[j] < arr[min_index]):
                min_index = j
        (array[i],array[min_index]) = (array[min_index],array[i])


arr = [-2, 45, 0, 11, -9,88,-97,-202,747]   
Selection_sort(arr,len(arr))

print(arr)


