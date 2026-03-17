class node2:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class rec2_list:
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
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def append(self,data):
        new_node = node2(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        new_node.next = None

    
    def remove(self):
        #remove the first element of the list
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        first_node = self.head
        self.head = first_node.next
        first_node.next = None
        self.head.prev = None


    def remove_end(self):
        #remove the last element of the list
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        last_node = self.tail
        self.tail = last_node.prev
        last_node.prev = None
        self.tail.next = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def length(self):
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
    
    def print_list_reverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev
