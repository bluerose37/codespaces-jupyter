def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = list(map(int,input("Enter numbers seperated by space: ").split()))
target = int(input("Enter number to search:"))

result = linear_search(arr,target)
print(f"Found at index 4 5 6 7 8 9{result}" if result != -1 else "Not found")
