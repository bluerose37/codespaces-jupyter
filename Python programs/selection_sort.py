def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):

        #Assume the current position holds the minimum element
        min_index=i

        #iterate through the unsorted portion to find the actual minimum
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:

                #update min_index if a smaller element is found
                min_index=j

        #move minimum element to its correct position
        arr[i],arr[min_index]=arr[min_index],arr[i]


def print_array(arr):
    for val in arr:
        print(val,end=" ")
    print()

if __name__=="__main__":
    arr=[64,23,14,45,67,56]

    print("Original array:",end="")
    print_array(arr)

    selection_sort(arr)

    print("Sorted array:",end="")
    print_array(arr)