import random
import time


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
    def __init__(self, elemnts_to_sort=None):
        if elemnts_to_sort is None:
            self.tab = []
        else:
            self.tab = elemnts_to_sort

        self.size = len(self.tab)

        if self.size > 0:
            self._build_heap()

    
    def _build_heap(self):
        for i in range(self.parent(self.size - 1), -1, -1):
            self.__repair_dequeue(i)
    
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

def selection_sort_swap(tab):
    n = len(tab)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]

def selection_sort_shift(tab):
    n = len(tab)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if tab[j] < tab[min_index]:
                min_index = j

        element = tab.pop(min_index)
        tab.insert(i, element)

    return tab

def test1():
    #test1
    dane_wejsciowe = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'),
                      (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]

    dane = [Node(value, key) for key, value in dane_wejsciowe]

    heap = Heap(dane)

    print("Kopiec jako tablica:")
    heap.print_tab()

    print("\nKopiec jako drzewo 2D:")
    heap.print_tree(0, 0)

    while not heap.is_empty():
        heap.dequeue()

    print("\nTablica po sortowaniu przez kopcowanie:")
    print(heap.tab)

    print("NIESTABILNE")

    #test swap
    print("\nTest sortowania przez wybieranie:\n")

    dane_swap = [Node(value, key) for key, value in dane_wejsciowe]
    selection_sort_swap(dane_swap)

    print("Sortowanie przez wybieranie - swap:")
    print(dane_swap)
    print("NIESTABILNE")

    #test shift
    dane_shift = [Node(value, key) for key, value in dane_wejsciowe]
    selection_sort_shift(dane_shift)

    print("\nSortowanie przez wybieranie - shift:")
    print(dane_shift)
    print("STABILNE")

def test2():
    print("\nTEST 2")

    dane = [int(random.random() * 100) for _ in range(10000)]

    dane_heap = dane[:]
    t_start = time.perf_counter()
    heap = Heap(dane_heap)
    while not heap.is_empty():
        heap.dequeue()
    t_stop = time.perf_counter()
    print("Czas sortowania przez kopcowanie:", t_stop - t_start)

    dane_swap = dane[:]
    t_start = time.perf_counter()
    selection_sort_swap(dane_swap)
    t_stop = time.perf_counter()
    print("Czas sortowania przez wybieranie (swap):", t_stop - t_start)

    dane_shift = dane[:]
    t_start = time.perf_counter()
    selection_sort_shift(dane_shift)
    t_stop = time.perf_counter()
    print("Czas sortowania przez wybieranie (shift):", t_stop - t_start)


if __name__ == "__main__":
    wybor = input("test do wykonania (1-2): ")
    if wybor == "1":
        test1()
    elif wybor == "2":
        test2()