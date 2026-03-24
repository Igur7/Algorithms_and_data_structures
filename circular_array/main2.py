CAPACITY = 6


class Node:
    def __init__(self):
        self.array = [None] * CAPACITY
        self.count = 0
        self.next = None

    def insert_at(self, index, value):
        if self.count >= CAPACITY:
            raise IndexError("Node is full")

        index = max(0, min(index, self.count))
        for i in range(self.count, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.count += 1

    def delete_at(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Node index out of range")

        value = self.array[index]
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.count - 1] = None
        self.count -= 1
        return value


class UnrolledLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        if index < 0:
            return None

        current = self.head
        while current is not None:
            if index < current.count:
                return current.array[index]
            index -= current.count
            current = current.next

        return None

    def insert(self, index, value):
        if index < 0:
            index = 0

        if self.head is None:
            self.head = Node()
            self.head.insert_at(0, value)
            return

        current = self.head
        prev = None

        while current is not None:
            if index <= current.count:
                break
            index -= current.count
            prev = current
            current = current.next

        if current is None:
            current = prev
            index = current.count

        if current.count < CAPACITY:
            current.insert_at(index, value)
            return

        next_node = Node()
        mid = CAPACITY // 2

        moved = 0
        for i in range(mid, current.count):
            next_node.array[moved] = current.array[i]
            current.array[i] = None
            moved += 1

        next_node.count = moved
        current.count = mid
        next_node.next = current.next
        current.next = next_node

        if index <= mid:
            current.insert_at(index, value)
        else:
            next_node.insert_at(index - mid, value)

    def delete(self, index):
        if index < 0:
            return None

        current = self.head
        prev = None

        while current is not None:
            if index < current.count:
                break
            index -= current.count
            prev = current
            current = current.next

        if current is None:
            return None

        deleted_value = current.delete_at(index)
        mid = CAPACITY // 2

        if current.count < mid and current.next is not None:
            next_node = current.next

            while current.count <= mid and next_node.count > 0:
                current.array[current.count] = next_node.delete_at(0)
                current.count += 1

            if next_node.count < mid:
                while next_node.count > 0 and current.count < CAPACITY:
                    current.array[current.count] = next_node.delete_at(0)
                    current.count += 1
                current.next = next_node.next

        if current.count == 0:
            if prev is None:
                self.head = current.next
            else:
                prev.next = current.next

        return deleted_value

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.array[:current.count], end="->")
            current = current.next
        print("None")


if __name__ == "__main__":
    ull = UnrolledLinkedList()

    for value in range(1, 10):
        ull.insert(value - 1, value)

    print(ull.get(4))

    ull.insert(1, 10)
    ull.insert(8, 11)
    ull.print_list()

    ull.delete(1)
    ull.delete(2)
    ull.print_list()
