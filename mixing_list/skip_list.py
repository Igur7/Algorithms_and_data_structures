import random 

class Node:
    def __init__(self, key, value,level,):
        self.key = key
        self.value = value
        self.level = level
        self.tab = [None] * level

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = Node(None, None, max_level)

    def randomLevel(p, maxLevel):
        lvl = 1   
        while random.random() < p and lvl <maxLevel:
            lvl = lvl + 1
        return lvl
    
    def search(self, key):
        current = self.head

        for lvl in range(self.max_level - 1,-1,-1):
            while current.tab[lvl] is not None and current.tab[lvl].key < key:
                current = current.tab[lvl]
        
        #schodze na zero w aktualnym nodzie
        current = current.tab[0]

        if current is not None and current.key == key:
            return current.data

        return None            
    
    def insert(self, key, data):
        update = [None] * self.max_level
        current = self.head

        for lvl in range(self.max_level - 1, -1, -1):
            while current.tab[lvl] is not None and current.tab[lvl].key < key:
                current = current.tab[lvl]
            update[lvl] = current

        current = current.tab[0]

        if current is not None and current.key == key:
            current.data = data
            return

        lvl = self.randomLevel(0.5, self.max_level)
        new_node = Node(key, data, lvl)

        for i in range(lvl):
            new_node.tab[i] = update[i].tab[i]
            update[i].tab[i] = new_node

    def remove(self, key):
        update = [None] * self.max_level
        current = self.head

        for lvl in range(self.max_level - 1 , -1, -1):
            while current.tab[lvl] is not None and current.tab[lvl].key < key:
                current = current.tab[lvl]
            update[lvl] = current
        
        current = current.tab[0]

        if current is not None and current.key == key:
            for i in range(current.level):
                if update[i].tab[i] != current:
                    break
                update[i].tab[i] = current.tab[i]
        del current
    
    def displayList_(self):
        node = self.head.tab[0] 
        keys = [ ]                       
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.data:2s}", end="")
                node = node.tab[lvl]
            print()
    
    def __str__(self):
        result = []
        node = self.head.tab[0]  

        while node is not None:
            result.append(f"({node.key}:{node.data})")
            node = node.tab[0]

        return "[" + ", ".join(result) + "]"
    
    