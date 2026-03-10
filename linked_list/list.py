            
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = None
            return
        last_node = self.head
        self.head = new_node
        new_node.next = last_node

    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = None
            return
        last_node = self.head 
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = None
    
    def remove(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            return
        last_node = self.head
        while last_node.next.next:
            last_node = last_node.next
        last_node.next = None

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.head is None:
            return 0
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count    

    def get(self):
        if self.head is None:
            return None
        return self.head.data


    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next 
        