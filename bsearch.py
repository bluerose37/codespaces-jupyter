def binary_search(arr,x):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=low+(high-low)//2
        
        if arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
    return -1

arr=[2,3,4,6,9,21,23,45,55,67,87,97,207]
x=67
result=binary_search(arr,x)

if result!=-1:
    print("Element is present at index",result)
else:
    print("Element is not present in array")
    
