class ChildNode:
    def __init__(self,key,value,right=None,left=None):
        self.key=key
        self.value=value
        self.right=right
        self.left=left

class BST:
    def __init__(self,root=None):
        self.root=root
    
    def search(self,key):
        first = self.root
        while first is not None:
            if first.key == key:
                return first.value
            elif first.key < key:
                first = first.right
            else:
                first = first.left  
        return None
    
    def insert(self,key,value):
        first = self.root
        if first is None:
            self.root = ChildNode(key,value)
            return
        
        while first is not None: 
            if first.key == key:
                first.value = value
                return
            elif first.key < key:
                if first.right is None:
                    first.right = ChildNode(key,value)
                    return
                else:
                    first = first.right
            else:
                if first.left is None:
                    first.left = ChildNode(key,value)
                    return
                else:
                    first = first.left

    def delete(self,key):
        first = self.root
        if first is None:
            return None
        while first is not None:
            if first.key == key:
                if first.left is None and first.right is None:
                    first = None
                    return
                elif first.left is not None and first.right is not None:
                    old = first
                    first = first.right
                    while first.left is not None:
                        first = first.left
                    old.key = first.key
                    old.value = first.value
                elif first.left is not None:
                    pass
                elif first.right is not None:
                    pass
            if first.key < key:
                first = first.right
            else:
                first = first.left
        return None
    
    def print_as_list(self):
        pass

    def print_tree(self):
        pass

    def height(self):
        pass