class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}:{self.value}"

class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for _ in range(size)]
        self.DELETED = object()
    
    def hash(self, key):
        if isinstance(key, str):
            key = sum(ord(znak) for znak in key)
        return key % self.size
    
    def probe(self, key, i):
        h = self.hash(key)
        return (h + self.c1 * i + self.c2 * i * i) % self.size

    def search(self, key):
        for i in range(self.size):
            
            index = self.probe(key, i)
            element = self.tab[index]

            if element is None:
                return None
            
            if element is self.DELETED:
                continue

            if element.key == key:
                return element.value
        return None
    
    def insert(self, key, value):
        for i in range(self.size):
            index = self.probe(key, i)
            element = self.tab[index]

            if element is None or element is self.DELETED:
                self.tab[index] = Element(key, value)
                return True

            if element.key == key:
                self.tab[index].value = value
                return True

        print("Brak miejsca")
        return False    
    
    def remove(self, key):
        for i in range(self.size):
            index = self.probe(key, i)
            element = self.tab[index]

            if element is None:
                print("Brak danej")
                return False

            if element is self.DELETED:
                continue

            if element.key == key:
                self.tab[index] = self.DELETED
                return True

        print("Brak danej")
        return False
    
    def __str__(self):
        elements = []
        for i in range(self.size):
            if self.tab[i] is None:
                elements.append("None")
            elif self.tab[i] is self.DELETED:
                elements.append("DELETED")
            else:
                elements.append(str(self.tab[i]))
        return "{" + ", ".join(elements) + "}"
