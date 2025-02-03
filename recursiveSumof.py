def find_sum(arr, n):
    
    if n == 0:
        return 0
    else:
        return arr[n-1] + find_sum(arr, n-1)

def find_max(arr, n):
    
    if n == 1:
        return arr[0]
    else:
        return max(arr[n-1], find_max(arr, n-1))

def find_min(arr, n):
    
    if n == 1:
        return arr[0]
    else:
        return min(arr[n-1], find_min(arr, n-1))

array = [1, 2, 3, 4]

sum_of_array = find_sum(array, len(array))
max_element = find_max(array, len(array))
min_element = find_min(array, len(array))

print(f"Sum: {sum_of_array}") 
print(f"Max: {max_element}")   
print(f"Min: {min_element}")  
