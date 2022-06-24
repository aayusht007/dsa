

# The Merge Sort algorithm is a sorting algorithm that is considered as an example of the divide and conquer strategy.
# it divides by 2 every time and sort the array by checking and comparing the elements of the array 

# THE TIME COMPLIXITY IS -  O(n LOG(n))
# it is a faster algorithms_available and commanly used


# def merge_sort(arr):
#     if len(arr)<=1:
#         return

#     mid=len(arr)//2

#     left=arr[:mid]
#     right=arr[mid:]

#     merge_sort(left)
#     merge_sort(right)
#     merge_two_elements(left,right,arr)
 

# def merge_two_elements(a,b,arr):
#     len_a=len(a)
#     len_b=len(b)

#     i=j=k=0

#     while i<len_a and j<len_b:
#         if a[i]<=b[j]:
#             arr[k]=a[i]
#             i+=1
#         else:
#             arr[k]=b[j]
#             j+=1
#         k+=1
        
#     while i<len_a:         
#             arr[k]=a[i]       # when the size of the aaray is not equal to the a!=b but the loop has to end so we use 
#             i+=1                 #this while loop for all  traversing all the elements
#             k+=1

#     while j<len_b:
#             arr[k]=b[j]
#             j+=1
#             k+=1
         


# if __name__ == '__main__':
#     test_cases = [
#         [10, 3, 15, 7, 8, 23, 98, 29],
#         [],
#         [3],
#         [9,8,7,2],
#         [1,2,3,4,5]
#     ]

#     for arr in test_cases:
#         merge_sort(arr)
#         print(arr)



###########################   EXCERSICE ######################################
# MERGE SORT USING DICT

def merge_sort(elements,key,descending=False):
    size=len(elements)
    if size==1:
        return elements
    mid=size//2
    left=merge_sort(elements[0:mid],key,descending)
    right=merge_sort(elements[mid:],key,descending)
    sorted=merge_two_elements(left,right,key,descending)

    return sorted



def merge_two_elements(left,right,key,descending=False):
    merge=[]
    if descending:

        while len(left)>0 and len(right)> 0:
            
            if left[0][key]>= right[0][key]:
                merge.append(left.pop(0))

            else:
                merge.append(right.pop(0))

    else:
        while len(left)>0 and len(right)>0:

            if left[0][key]<right[0][key]:
                merge.append(left.pop(0))
            else:
                merge.append(right.pop(0))

    merge.extend(left)
    merge.extend(right)
    return merge

        

        

if __name__=="__main__":
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    new=merge_sort(elements,key='name',descending=False)
    print(new)
