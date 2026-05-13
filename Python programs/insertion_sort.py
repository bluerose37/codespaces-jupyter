def insertion_sort(arr):
    for i in range (1,len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

if __name__=="__main__":
    arr=[23,45,12,37,76,89,56]
    insertion_sort(arr)
    print_array(arr)