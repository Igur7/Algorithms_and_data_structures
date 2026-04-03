from AVL import AVL

AVL1 = AVL()

elements = {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}
for key, value in elements.items():
    AVL1.insert(key, value)

print("Drzewo 2D:")
AVL1.print_tree()

print("Lista elementów:", AVL1.print_as_list())

print("Wartość dla klucza 10:", AVL1.search(10))

AVL1.delete(50)
AVL1.delete(52)
AVL1.delete(11)
AVL1.delete(57)
AVL1.delete(1)
AVL1.delete(12)

AVL1.insert(3, 'AA')
AVL1.insert(4, 'BB')

AVL1.delete(7)
AVL1.delete(8)

print("Drzewo 2D po operacjach:")
AVL1.print_tree()

print("Lista elementów po operacjach:", AVL1.print_as_list())