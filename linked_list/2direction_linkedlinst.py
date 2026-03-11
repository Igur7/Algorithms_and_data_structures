class node2:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class linked_list_2directional:
    def __init__(self):
        self.head = None
        self.tail = None

    def destroy(self):
        self.head = None
        self.tail = None

    def add(self,data):
        new_node = node2(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
            return
        new_node.next = self.head

    def append(self,data):
        pass
    
    def remove(self):
        pass

    def remove_end(self):
        pass
    def is_empty(self):
        pass

    def length(self):
        pass    

    def get(self):
        pass


    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next 
    
