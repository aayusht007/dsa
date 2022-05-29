# to del a element there are 2 approaches
# 1. if there is leaf node
# 2. if there us only one child
# 3. if there are two childs

# 1.. take the max value from the right and min val form left node and replace it with the node that you want to del 
# because their will be element greater element present in left side and smaller element present in right side.

from xml.dom.minidom import Element


class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    def add_child(self,elem):
        if elem==self.data:
            return #already exits there can be only one elem

        if elem>self.data:
            if self.right:
                self.right.add_child(elem)
            else:
                self.right=BinaryTree(elem)

        if elem<self.data:
            if self.left:
                self.left.add_child(elem)
            else:
                self.left=BinaryTree(elem)

    def search(self,val):
        if self.data==val:
            return True
        
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def max_val(self):
        if self.right==None:
            return self.data
        else:
            return self.right.max_val()

    def min_val(self):       
        if self.left==None:
            return self.data
        else:
            return self.left.min_val()

    def sum_add(self):
        left_sum=self.left.sum_add() if self.left else 0
        right_sum=self.right.sum_add() if self.right else 0
        return left_sum+right_sum+self.data

    def in_order_traversal(self):
        element=[]
        if self.left:
            element+=self.left.in_order_traversal()
        element.append(self.data)
        if self.right:
            element+=self.right.in_order_traversal() 

        return element

    def delete(self,elem):
        if elem>self.data:
            if self.right:
                self.right=self.right.delete(elem)
        elif elem<self.data:
            if self.left:
                self.left=self.left.delete(elem)
        else:
            if self.right==None and self.left==None:
                return None
            elif self.left==None:
                return self.right
            elif self.right==None:
                return self.left

            max_value=self.right.max_val()
            self.data=max_value
            self.right=self.right.delete(max_value)
        
        return self

def show_tree(element):
    print(f"the tree contains {element}")
    root=BinaryTree(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])
    return root

if __name__=="__main__":
    no = show_tree([17, 4, 1, 20, 9, 23, 18, 34])
    no.delete(20)
    # print(no.sum_add())
    print("After deleting 20 ",no.in_order_traversal())
    numbers_tree = show_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]
