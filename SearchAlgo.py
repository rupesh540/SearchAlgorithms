def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
        
    return "Not Present"
	
def binary_search(arr, low, high, item):
    if low <= high:
        mid = (low+high)//2
        print ("mid value is", arr[mid])
        
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr, low, mid-1, item)
        else:
            return binary_search(arr, mid+1, high, item)
        
    else:
        return "Not Present"
        
def is_sorted(arr):
    
    sorted = True
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
        
    return sorted
            
import random
import time
def monkey_sort(arr):
    
    while not is_sorted(arr):
        random.shuffle(arr)
        print(arr)
        time.sleep(1)
    print(arr)