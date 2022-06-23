
# quick sort is defined as sorting done by partition. // partion is define as taking pivot element in between the array and making 2 side 
# of array left and right [6,3,7,4,5,10] 6 is pivot elment [3,4,5,6,7,10] 
# there are two methods hoare and lomotu partitioning 
# in hoare there is start= pivot+1 and end 
# // time complexcity is o(nlogn)
# // worst case complexity is o(n^2)


def sort(a,b,arr):
    tmp=arr[a]
    arr[a]=arr[b]
    arr[b]=tmp


def quicksort(elements,start,end):
    if start<end:

        pi=partition(elements,start,end)
        quicksort(elements,pi+1,end)#RIGHT partation
        quicksort(elements,start,pi-1)#left partitiom


def partition(elements,start,end):
    pivot_pos=start
    pivot=elements[pivot_pos]

    while start<end:
        while start<len(elements) and elements[start]<=pivot:
            start+=1

        while elements[end]>pivot:
            end-=1

        if start<end:
            sort(start,end,elements)
    sort(pivot_pos,end,elements)
    return end
    



if __name__=="__main__":
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quicksort(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    for elements in tests:
        quicksort(elements, 0, len(elements)-1)
        print(f"the ans are {elements}")