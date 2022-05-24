
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def show(self):
        if self.head is None:
            print('linked list is empty')
            return

        itr=self.head
        llstr=''
        while itr:
            llstr+= str(itr.data)+'-->'
            itr=itr.next
        print(llstr)

    def find_len(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count



    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,next=None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    
    def insert_at(self,index,data):
        if index<0 or index>self.find_len():
            raise Exception("invalid index")

        if index==0:
            self.insert_at_begining(data)
            return

        if index== -1:
            self.insert_at_end(data)
            return

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break

            itr=itr.next
            count+=1

    def remove_at(self,index):
        if index<0 or index>self.find_len():
            raise Exception("invalid index")

        if index==0:
            self.head=self.head.next
            return
        
        count=0
        itr=self.head
        while itr:
            if count== index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def insert_values(self,values):
        self.head== None
        for data in values:
            self.insert_at_end(data)




    def insert_after_values(self,data_after,data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return

        itr=self.head
        while itr:
            if itr.data== data_after:
                itr.next=Node(data_to_insert,itr.next)
                break

            itr=itr.next


    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data== data:
            self.head=self.head.next
            return

        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break

            itr=itr.next
  




if __name__ == '__main__':
    ll=Linkedlist()
    ll.insert_at_begining(5)  
    ll.insert_at_begining(3)
    ll.insert_at_begining(6)
    # ll.show()
    # ll.insert_at(3,'aaysuh')
    # ll.remove_at(1)
    # ll.insert_values([2,3,4,5,6])
    # ll.show()
    # ll.insert_after_values(4,22)
    # ll.show()
    # ll.remove_by_value(4)
    ll.show()
    print(f'{ll.find_len()}')