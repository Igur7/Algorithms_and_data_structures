class Node:
    def __init__(self,data,priority):
        self.__dane = data
        self.__priorytet = priority
    
    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __gt__(self, other):
        return self.__priorytet > other.__priorytet
    
    def __repr__(self):
        return f"{self.__priorytet} : {self.__dane}"
        
class Heap:
    def __init__(self):
        self.tab = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.tab[0],self.tab[self.size-1] = self.tab[self.size-1],self.tab[0]
            self.size -= 1
            self.__repair_dequeue(0)
            return self.tab[self.size]

    def enqueue(self, node):
        if self.size == len(self.tab):
            self.tab.append(node)
        else:
            self.tab[self.size] = node
        self.size += 1
        id = self.size - 1
        self.__repair_enqueue(id)
        
    def left(self,id):
        left = 2 * id + 1
        return left 
    
    def right(self,id):
        right = 2 * id + 2
        return right
    
    def parent(self,id):
        parent = (id - 1) // 2
        return parent
    
    def __repair_dequeue(self,index = 0):
        while True:
            left = self.left(index)
            right = self.right(index)
            if left >= self.size:
                break
            if right >= self.size:
                if self.tab[index] < self.tab[left]:
                    self.tab[index],self.tab[left] = self.tab[left],self.tab[index]
                break
            if self.tab[index] < self.tab[left] and self.tab[index] < self.tab[right]:
                if self.tab[right] > self.tab[left]:
                    self.tab[right],self.tab[index] = self.tab[index],self.tab[right]
                    index = right
                else:
                    self.tab[left],self.tab[index] = self.tab[index],self.tab[left]
                    index = left
            elif self.tab[index] < self.tab[left]:
                self.tab[left],self.tab[index] = self.tab[index],self.tab[left]
                index = left
            elif self.tab[index] < self.tab[right]:
                self.tab[right],self.tab[index] = self.tab[index],self.tab[right]
                index = right
            else:
                break

    def __repair_enqueue(self,index = 0):
        while index > 0:
            parent = self.parent(index)

            if self.tab[index] > self.tab[parent]:
                self.tab[index],self.tab[parent] = self.tab[parent],self.tab[index]
                index = parent
            else:
                break
    
    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')
    
    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx])
            self.print_tree(self.left(idx), lvl + 1)

if __name__ == "__main__":
    heap = Heap()
    priorytety = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    napis = "GRYMOTYLA"
    for i in range(len(priorytety)):
        heap.enqueue(Node(napis[i], priorytety[i]))
    
    heap.print_tree(0, 0)
    heap.print_tab()
    zwrot1 = heap.dequeue()
    print(heap.peek())
    heap.print_tab()
    print("zwort1:")
    print(zwrot1)
    print("Zawartość kopca po usunięciu elementu o najwyższym priorytecie:")
    while not heap.is_empty():
        print(heap.dequeue())
    heap.print_tab()
