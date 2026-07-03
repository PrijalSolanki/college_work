def lower_bound(arr, target):
    low, high = 0, len(arr) - 1
    ans = len(arr)  
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1  
        else:
            low = mid + 1  
    return ans
arr = [25000, 32000, 41000, 50000, 50000, 65000, 70000]
target = 50000

index = lower_bound(arr, target)
print(index)        
print(arr[index])