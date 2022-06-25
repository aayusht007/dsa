
selection sort is selection a first elements as i and next element as j and matching each element

complexity= O(n^2)

# def selection_sort(arr):
#     size=len(arr)
#     for i in range(size-1):
#         min_index=i
#         for j in range(min_index+1,size):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         if i!= min_index:
#             arr[i],arr[min_index]=arr[min_index],arr[i]
        


# if __name__ == '__main__':
#     tests = [
#         # [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
#         # [],
#         # [1,5,8,9],
#         [234,3,1,56,34,12,9,12,1300],
#         [78, 12, 15, 8, 61, 53, 23, 27],
#         [5]
#     ]
#     for elements in tests:
#         selection_sort(elements)
#         print(elements)


  ##################################  EXCERSICE USING DICT   ###################################


def selection_sort(arr,key):
    size=len(arr)
    for i in range(size-1):
        min_index=i
        for j in range(min_index+1,size):
            if arr[j][key]<arr[min_index][key]:
                min_index=j
        if i!=min_index:
            arr[i],arr[min_index]=arr[min_index],arr[i]






if __name__=='__main__':
    elements=[
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    selection_sort(elements,key="Last Name")
    print(elements)