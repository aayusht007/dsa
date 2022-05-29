from xml.dom.minidom import Element


class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return
        
        if data<self.data:
            if self.left:
                #to add in left side
                self.left.add_child(data)
            else:
                #if there is no left
                self.left=BinarySearchTree(data)
        
        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)

    def search(self,val):
        if self.data==val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
        else:
            return False

        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
        
    def pre_order_tarversal(self):
        element=[]
        element.append(self.data)
        if self.left:
            element+=self.left.pre_order_tarversal()
        if self.right:
            element+=self.right.pre_order_tarversal()
        
        return element

    def post_order_traversal(self):
        element=[]
        if self.left:
            element+=self.left.post_order_traversal()
        if self.right:
            element+=self.right.post_order_traversal()
        
        element.append(self.data)

        return element

    def in_order_traversal(self):
        element=[]
        #for left side
        if self.left:
            element+=self.left.in_order_traversal()
        #for root node 
        element.append(self.data)
        #for right node
        if self.right:
            element+=self.right.in_order_traversal()

        return element
    
    def sum_add(self):
        left_sum=self.left.sum_add() if self.left else 0
        right_sum=self.right.sum_add() if self.right else 0
        return left_sum+right_sum+self.data

def build_tree(elements):
    print(f" building tree with these elements{elements}")
    root=BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ =="__main__":
    no=[17, 4, 1, 20, 9, 23, 18, 34]
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    new=build_tree(no)
    print(new.sum_add())
    print(new.post_order_traversal())
    print(new.pre_order_tarversal())
