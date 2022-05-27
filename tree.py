
# class TreeNode:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]
#         self.parent=None

#     def add_child(self,child):
#         child.parent=self #self is parent of child
#         self.children.append(child)

#     def get_level(self):
#         level=0
#         p =self.parent
#         while p:
#             level+=1
#             p=p.parent
#         return level

#     def print_tree(self):
#         spaces=" "* self.get_level() *3
#         prefix=spaces+ "|__" if self.parent else""

#         print(prefix+self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()

# def build_product_tree():
#     root=TreeNode("electronics")
    
#     laptop=TreeNode('laptop')
#     laptop.add_child(TreeNode('mac'))
#     laptop.add_child(TreeNode('thinkpad'))
#     laptop.add_child(TreeNode('surface'))

#     cellphone=TreeNode('cell phone')
#     cellphone.add_child(TreeNode('iphone'))
#     cellphone.add_child(TreeNode('realme'))
#     cellphone.add_child(TreeNode('vivo'))

#     tv=TreeNode('tv')
#     tv.add_child(TreeNode('lg'))
#     tv.add_child(TreeNode('mi'))
#     tv.add_child(TreeNode('samsung'))

#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)
#     root.print_tree()


# if __name__=='__main__':
#     build_product_tree()


 #excercise 1

# from dataclasses import dataclass


# class TreeNode:
#     def __init__(self,data,name):
#         self.data=data
#         self.name=name
#         self.children=[]
#         self.parent=None

#     def add_child(self,child):
#         child.parent=self
#         self.children.append(child)

#     def get_level(self):
#         p=self.parent
#         level=0
#         while p:
#             level+=1
#             p=p.parent
#         return level


#     def print_tree(self,property_name):
#         if property_name=="both":
#             value=self.data+self.name+"(" +self.name+")"
#         elif property_name=="name":
#             value=self.name
#         elif property_name=="data":
#             value=self.data

#         spaces=" " * self.get_level() * 5
#         valid=spaces+"|__" if self.parent else ""


#         print(valid+value)
#         if self.children:
#             for child in self.children:
#                 child.print_tree(property_name)

# def build_tree():
#     root=TreeNode("ceo",'aayush')
#     cto=TreeNode('cto','piyush')
#     infra_head=TreeNode('infrastructure head','aa')
#     infra_head.add_child(TreeNode('cloud manager','bb'))
#     infra_head.add_child(TreeNode('app manager','cc'))
#     cto.add_child(TreeNode('aplication head','dd'))
#     cto.add_child(infra_head)

#     hr_head=TreeNode("hr_head",'ss')
#     hr_head.add_child(TreeNode('recruitment head','ss'))        
#     hr_head.add_child(TreeNode('policy head','kk'))
#     root.add_child(hr_head)
#     root.add_child(cto)
#     return root

# if __name__=='__main__':
#     no=build_tree()
#     no.print_tree("both")


# excercise 3-______

# from pyrsistent import T


# class Tree:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]
#         self.parent=None

#     # def get_level(self):
#     #     level=0
#     #     p=self.parent
#     #     while p:
#     #         level+=1
#     #         p=p.parent

#     #     return level

    

#     def add_child(self,child):
#         child.parent=self
#         self.children.append(child)

#     # def print_tree(self,level):
#     #     if self.get_level() > level:
#     #         return
            
#     #     spaces=" " * self.get_level() * 3
#     #     valid=spaces +"|__" if self.parent else ""
        
#     #     print(valid + self.data)
#     #     if self.children:
#     #         for child in self.children:
#     #             child.print_tree(level)
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent

#         return level

#     def print_tree(self, level):
#         if self.get_level() > level:
#             return
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree(level)
        
# def show_tree():
#     root=Tree("Global")

#     india=Tree("India")

#     gujrat=Tree("Gujrat")
#     gujrat.add_child(Tree('Ahamdabad'))
#     gujrat.add_child(Tree('varoda'))

#     Karnataka=Tree("karnataka")
#     Karnataka.add_child(Tree("bangalore"))
#     Karnataka.add_child(Tree("Mysore"))

#     india.add_child(Tree(gujrat))
#     india.add_child(Tree(Karnataka))

#     usa=Tree("usa")
#     # usa.add_child(Tree(newjersy))
#     # usa.add_child(Tree(california))
#     california=Tree("california")
#     newjersy=Tree("New jersy")
#     newjersy.add_child(Tree("Princeton"))
#     newjersy.add_child(Tree("Trenton"))

#     california.add_child(Tree("san francisco"))
#     california.add_child(Tree("mountain view"))
#     california.add_child(Tree("palo alto"))

#     usa.add_child(Tree(newjersy))
#     usa.add_child(Tree(california))

#     root.add_child(Tree(india))
#     root.add_child(Tree(usa))
#     return root

# if __name__ =="__main__":
#     no=show_tree()
#     no.print_tree(3)

######################## correct prob 3

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(3)
