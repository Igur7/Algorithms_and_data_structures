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
    
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.array[self.read_idx]
        self.array[self.read_idx] = None
        self.read_idx = (self.read_idx + 1) % self.size
        return value
    

    def enqueue(self, value) -> None:
        self.array[self.write_idx] = value
        self.write_idx = (self.write_idx + 1) % self.size

        if self.write_idx == self.read_idx:
            self._resize()

    def _resize(self) -> None:
        old_array = self.array
        old_size = self.size
        new_size = old_size * 2
        new_array = [None for _ in range(new_size)]

        if self.write_idx == self.read_idx:
            count = old_size
        elif self.write_idx > self.read_idx:
            count = self.write_idx - self.read_idx
        else:
            count = old_size - (self.read_idx - self.write_idx)

        for i in range(count):
            new_array[i] = old_array[(self.read_idx + i) % old_size]

        self.array = new_array
        self.size = new_size
        self.read_idx = 0
        self.write_idx = count

    def _count(self) -> int:
        if self.write_idx >= self.read_idx:
            return self.write_idx - self.read_idx
        return self.size - (self.read_idx - self.write_idx)

    def __str__(self) -> str:
        count = self._count()
        elements = [self.array[(self.read_idx + i) % self.size] for i in range(count)]
        return "[" + ", ".join(str(el) for el in elements) + "]"

    def table_state(self):
        """Zwraca kopię wewnętrznej tablicy dla celów testowych."""
        return list(self.array)