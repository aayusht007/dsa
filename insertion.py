# insertion sort which sort the array in one does not require any other to save it 


def insertion_sort(elements):
    for i in range(1,len(elements)):
        anchor=elements[i]
        j=i-1
        while j>=0 and elements[j]>anchor:
            elements[j+1]=elements[j]
            j-=1
        elements[j+1]=anchor
    
    return elements



if __name__=="__main__":
    elements=[11,9,29,7,2,15,28]
    print(insertion_sort(elements))




# def insertion_sort(elements):
#     for i in range(1,len(elements)):
#         anchor=elements[i]
#         j=i-1
#         while elements[j]>anchor and j>=0:
#             elements[j+1]=elements[j]
#             j=j-1
#         elements[j+1]=anchor


# if __name__=="__main__":
#     elements=[11,9,29,7,2,15,28]
#     insertion_sort(elements)
#     print(elements)
