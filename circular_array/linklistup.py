NODE_CAPACITY = 6  # globalna zmienna określająca rozmiar tablicy w węźle


class Node:
    """Element rozwiniętej listy wiązanej."""

    def __init__(self):
        self.array = [None] * NODE_CAPACITY
        self.count = 0          # aktualne wypełnienie
        self.next: "Node | None" = None

    def insert_at(self, index: int, value) -> None:
        """Wstaw wartość pod lokalny indeks (0 ≤ index ≤ count).
        Zakłada, że jest wolne miejsce (count < NODE_CAPACITY)."""
        for i in range(self.count, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.count += 1

    def delete_at(self, index: int):
        """Usuń i zwróć wartość spod lokalnego indeksu (0 ≤ index < count)."""
        value = self.array[index]
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.count - 1] = None
        self.count -= 1
        return value


class UnrolledLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.size = 0  # łączna liczba elementów w liście


    def _find_node_and_local_index(self, global_index: int):
        """Zwraca (węzeł, lokalny_indeks) dla podanego globalnego indeksu.
        Jeśli global_index ≥ size, zwraca ostatni węzeł z lokalnym indeksem
        równym jego count (wstawienie na końcu)."""
        node = self.head
        remaining = global_index
        prev = None

        while node is not None:
            if remaining < node.count:
                return node, remaining, prev
            remaining -= node.count
            if node.next is None:
                # Wyszliśmy poza listę – wróć do końca tego węzła
                return node, node.count, prev
            prev = node
            node = node.next

        # Lista pusta
        return None, 0, None

    def get(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError(f"Indeks {index} poza zakresem listy (size={self.size})")
        node, local_idx, _ = self._find_node_and_local_index(index)
        return node.array[local_idx]


    def insert(self, index: int, value) -> None:
        # Ogranicz indeks do rozmiaru listy
        if index > self.size:
            index = self.size

        # Specjalny przypadek: lista pusta
        if self.head is None:
            self.head = Node()
            self.head.insert_at(0, value)
            self.size += 1
            return

        node, local_idx, prev = self._find_node_and_local_index(index)

        if node.count < NODE_CAPACITY:
            # Jest miejsce – wstaw bezpośrednio
            node.insert_at(local_idx, value)
        else:
            # Węzeł pełny – split: przenosimy połowę do nowego węzła
            new_node = Node()
            half = NODE_CAPACITY // 2

            # Przenosimy drugą połowę tablicy do nowego węzła
            for i in range(half, NODE_CAPACITY):
                new_node.array[i - half] = node.array[i]
                node.array[i] = None
            new_node.count = NODE_CAPACITY - half
            node.count = half

            # Podłącz nowy węzeł
            new_node.next = node.next
            node.next = new_node

            # Zdecyduj, do którego węzła wstawić
            if local_idx <= half:
                node.insert_at(local_idx, value)
            else:
                new_node.insert_at(local_idx - half, value)

        self.size += 1

    def delete(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError(f"Indeks {index} poza zakresem listy (size={self.size})")

        node, local_idx, prev = self._find_node_and_local_index(index)
        value = node.delete_at(local_idx)
        self.size -= 1

        half = NODE_CAPACITY // 2

        # Jeśli węzeł zapełniony poniżej połowy i istnieje następnik
        if node.count < half and node.next is not None:
            next_node = node.next

            # Ile elementów trzeba przenieść, aby przekroczyć połowę?
            # Chcemy node.count > half, więc potrzebujemy (half - node.count + 1) elementów
            needed = half - node.count + 1
            to_move = min(needed, next_node.count)

            for _ in range(to_move):
                moved_val = next_node.delete_at(0)
                node.array[node.count] = moved_val
                node.count += 1

            # Sprawdź, czy po przeniesieniu następnik jest pusty lub spełnia warunek scalenia
            # Specyfikacja: jeśli po przeniesieniu wypełnienie następnika < half
            # ORAZ wszystkie elementy następnika zmieszczą się w bieżącym węźle → scal
            if next_node.count < half and node.count + next_node.count <= NODE_CAPACITY:
                # Przenieś wszystko z next_node do node
                for i in range(next_node.count):
                    node.array[node.count] = next_node.array[i]
                    node.count += 1
                # Usuń next_node z listy
                node.next = next_node.next

        return value


    def print_list(self) -> None:
        parts = []
        node = self.head
        while node is not None:
            parts.append(str(node.array))
            node = node.next
        print(" -> ".join(parts))
        


if __name__ == "__main__":
    ull = UnrolledLinkedList()

    for i in range(1, 10):
        ull.insert(ull.size, i)

    print(ull.get(4))

    ull.insert(1, 10)
    ull.insert(8, 11)
    ull.print_list()

    ull.delete(1)
    ull.delete(2)
    ull.print_list()