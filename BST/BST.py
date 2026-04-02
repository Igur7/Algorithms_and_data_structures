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
            return


        if first.left is None and first.right is None and first.key == key:
            self.root = None
            return
        
        previous = None

        while first is not None and first.key != key:
            previous = first
            if key < first.key:
                first = first.left
            else:
                first = first.right
        
        if first is None:
            return 
        
        if first.left is None and first.right is None:
            if previous.left == first:
                previous.left = None
            else:
                previous.right = None

            first = None

        elif first.right is None and first.left is not None:
            if previous.right == first:
                previous.right = first.left
            elif previous.left == first:
                previous.left = first.left

            first = None

        elif first.left is None and first.right is not None:
            if previous.right == first:
                previous.right = first.right
            elif previous.left == first:
                previous.left = first.right

            first = None
        
        elif first.left is not None and first.right is not None:
            successor = first.right
            successor_parent = first

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            
            if successor_parent != first:
                successor_parent.left = successor.right
                successor.right = first.right
            
            if previous is None:
                self.root = successor
            elif previous.left == first:
                previous.left = successor
            else:
                previous.right = successor
            
            successor.left = first.left
            first = None

    
    def print_as_list(self):
        pass

    def print_tree(self):
        pass

    def height(self):
        pass