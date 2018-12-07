def counting_sort(arr):

    a = min(arr)
    b = max(arr)

    cumulative_counter = 0
    corresponding_array = {}

    for i in range(a,b+1):
        cumulative_counter+=arr.count(i)
        corresponding_array[i] = cumulative_counter

    mirror_arr = arr.copy()

    for i in range(b,a,-1):
        corresponding_array[i] = corresponding_array[i-1]
    
    corresponding_array[a] = 0

    for i in mirror_arr:
        arr[corresponding_array[i]] = i
        corresponding_array[i]+=1
    
    return arr
