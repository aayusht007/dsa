
# space complexity of o(1)
# TIME COMLEXITY of :: o(n^2)

# In bubble sort we take 2 element and swap them one by having n-1 iteration and having 2 loops having TIME COMLEXITY of :: o(n^2) because of 2 loops and 
# space complexity of o(1)== because of one array in which we loop again and Again
# // it is known as bubble sort because bubble pops from down bottom to upper layer like here thw highes element goes from top to bottom 

# def bubblesort(elements):
#     size=len(elements)
#     for i in range(size-1):
#         swapped=False
#         for j in range(size-1-i):
#             if elements[j]>elements[j+1]:
#                 tmp=elements[j]
#                 elements[j]=elements[j+1]
#                 elements[j+1]=tmp
#                 swapped=True
#         if not sorted:
#             break
#     return elements




def bubblesort_dict(elements,key):
    size=len(elements)
    for i in range(size-1):
        swapped=0
        for j in range((size-1)-i):
            if elements[j][key]> elements[j+1][key]:
                tmp=elements[j][key]
                elements[j][key]=elements[j+1][key]
                elements[j+1][key]=tmp
                swapped=1
        if not swapped:
            break
    return elements   



# if __name__=="__main__":
#     elements = [5,9,2,1,67,34,88,34]
#     elements = [1,2,3,4,2]
#     # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
#     print(bubblesort(elements))

############excercise##################
if __name__=='__main__':
    elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
    print(bubblesort_dict(elements,'transaction_amount'))