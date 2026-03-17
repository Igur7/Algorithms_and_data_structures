class CircularQueue:

    def __init__(self, initial_capacity: int = 5) -> None:
        self.size = initial_capacity
        self.array = [None for _ in range(self.size)]
        self.read_idx = 0
        self.write_idx = 0

    def is_empty(self) -> bool:
        return self.read_idx == self.write_idx  
    
    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.read_idx]
    
    def deqeueue(self):
        if self.is_empty():
            return None
        

