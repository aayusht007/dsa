# binary searching is a technique in which there evert time no is divided by 2 
# time complexity of normal search is o(n)
# time complexity of binary search is iteration n/2 and 2nd is n/2/2=n2^2 so  for k iteration 1= n/2^k 
# k=log(n)   o(log n)

from email.mime.audio import MIMEAudio
from numpy import number
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        new=func(*args,**kwargs)
        end=time.time()
        print(f"the time of {func.__name__} is {(end-start)*10000}")
        return new
    return wrapper

@time_it
def linear_search(number_list,number_to_search):
    for index,element in enumerate(number_list):
        if element==number_to_search:
            return index
    return -1

@time_it
def binary_search(number_list,number_to_search):
    left_index=0
    right_index=len(number_list)-1
    mid_index =0

    while left_index<=right_index:
        mid_index=(left_index+right_index)//2
        mid_number=number_list[mid_index]

        if mid_number==number_to_search:
            return mid_index
        if mid_number<number_to_search:
            left_index=mid_index+1
        else:
            right_index=mid_index-1

    return -1

def recursive_binarysearch(number_list,number_to_search,left_index,right_index):
    if left_index>right_index:
        return -1
    mid_index=(left_index+right_index)//2
    mid_no=number_list[mid_index]
    if mid_index<0 or mid_index>len(number_list):
        return -1

    if mid_no==number_to_search:
        return mid_index

    if mid_no<number_to_search:
        left_index=left_index+1
    else:
        right_index=right_index-1

    return recursive_binarysearch(number_list,number_to_search,left_index,right_index)

def all_occurance(number,number_to_search):
    index=binary_search(number,number_to_search)
    indeces=[index]
    # find indices on left side
    i=index-1
    while i>=0:
        if number[i]==number_to_search:
            indeces.append(i)
        else:
            break
        
        i=i-1

    i=index+1
    while i<len(number):
        if number[i]==number_to_search:
            indeces.append(i)
        else:
            break
        i=i+1
    
    return(sorted(indeces))





if __name__=="__main__":
    # number_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_search = 67
    # print(linear_search(number_list,number_to_search))
   
    # print(binary_search(number_list,number_to_search))
    # # index = recursive_binarysearch(number_list, number_to_search, 0, (len(number_list)-1))
    # # print(index)
    number = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_search = 15
    indice = all_occurance(number, number_to_search)
    print(indice)