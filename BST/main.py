from BST import BST

BST1 = BST()

elements = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
for key, value in elements.items():
    BST1.insert(key, value)

print("Drzewo 2D początkowe:")
BST1.print_tree()
print("Lista elementów:", BST1.print_as_list())

print("Wartość dla klucza 24:", BST1.search(24))

BST1.insert(20, 'AA')

BST1.insert(6, 'M')

BST1.delete(62)

BST1.insert(59, 'N')
BST1.insert(100, 'P')

BST1.delete(8)
BST1.delete(15)

BST1.insert(55, 'R')

BST1.delete(50)
BST1.delete(5)
BST1.delete(24)

print("Wysokość drzewa:", BST1.height())

print("Zawartość drzewa jako lista:", BST1.print_as_list())

print("Drzewo 2D po operacjach:")
BST1.print_tree()