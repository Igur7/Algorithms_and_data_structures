class ChildNode:
    def __init__(self,key,value,right=None,left=None):
        self.key=key
        self.data=value
        self.right=right
        self.left=left
        self.height=1

class AVL:
    def __init__(self,root=None):
        self.root=root
    
    def _rotate_right(self, pkt):
        x = pkt.left
        pkt.left = x.right

        x.right = pkt

        self._update_height(pkt)
        self._update_height(x)

        return x
    
    def _rotate_left(self, pkt):
        y = pkt.right
        pkt.right = y.left

        y.left = pkt

        self._update_height(pkt)
        self._update_height(y)

        return y
    
    def _balance(self,node):
        self._update_height(node)
        bf = self._get_balance_factor(node)
        
        if bf == 2:
            if self._get_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
            else:
                return self._rotate_right(node)
    
        if bf == -2:
            if self._get_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
            else:
                return self._rotate_left(node)
        return node
    
    def search(self,key):
        first = self.root
        while first is not None:
            if first.key == key:
                return first.data
            elif first.key < key:
                first = first.right
            else:
                first = first.left  
        return None
    
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return ChildNode(key, value)
        
        if key == node.key:
            node.data = value
            return node
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)
        
        return self._balance(node)

    def delete(self, key):
        first = self.root

        if first is None:
            return

        if first.left is None and first.right is None and first.key == key:
            self.root = None
            return
        
        path = []
        previous = None

        while first is not None and first.key != key:
            path.append(first)
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
            if previous is None:
                self.root = first.left
            elif previous.right == first:
                previous.right = first.left
            elif previous.left == first:
                previous.left = first.left
            first = None

        elif first.left is None and first.right is not None:
            if previous is None:
                self.root = first.right
            elif previous.right == first:
                previous.right = first.right
            elif previous.left == first:
                previous.left = first.right
            first = None
        
        elif first.left is not None and first.right is not None:
            path.append(first) 
            successor = first.right
            successor_parent = first

            while successor.left is not None:
                path.append(successor)
                successor_parent = successor
                successor = successor.left
            
            first.key = successor.key
            first.data = successor.data

            if successor_parent == first:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right

        while path:
            node = path.pop()
            balanced = self._balance(node)
            if path:
                parent = path[-1]
                if parent.left is node:
                    parent.left = balanced
                else:
                    parent.right = balanced
            else:
                self.root = balanced

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self.__print_tree(node.left, lvl+5)

    def print_as_list(self):
        result = []
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(f"{current.key}:{current.data}")  
            current = current.right

        return ",".join(result)
    
    def _get_height(self, node):
        if node is not None:
            return node.height
        else:
            return 0
        
    def _update_height(self, node):
        max_height = max(self._get_height(node.left), self._get_height(node.right))
        node.height = max_height + 1
    
    def _get_balance_factor(self, node):
        if node is not None:
            return self._get_height(node.left) - self._get_height(node.right)
        else:
            return 0
        
    def height(self):
        return self.__height(self.root)
    
    def __height(self, node):
        if node is None:
            return 0
        
        left_height = self.__height(node.left)
        right_height = self.__height(node.right)

        return max(left_height, right_height) + 1
        