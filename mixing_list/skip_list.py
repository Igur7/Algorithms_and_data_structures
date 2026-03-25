import random 

class Node:
    def __init__(self, key, value,level,):
        self.key = key
        self.value = value
        self.level = level
        self.tab = [None] * level

    def __str__(self):
        return f"{self.key}:{self.value}"

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
        while self.head:
            
    
    def insert(self, key, value):
        pass
    
    def remove(self, key):
        pass
    
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