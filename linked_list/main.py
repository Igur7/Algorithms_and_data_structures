import linked_list.listl as listl

unis = [('AGH', 'Kraków', 1919),
('UJ', 'Kraków', 1364),
('PW', 'Warszawa', 1915),
('UW', 'Warszawa', 1915),
('UP', 'Poznań', 1919),
('PG', 'Gdańsk', 1945)]

uczelnie = listl.linked_list()

uczelnie.append(unis[0])
uczelnie.append(unis[1])
uczelnie.append(unis[2])

uczelnie.add(unis[3])
uczelnie.add(unis[4])
uczelnie.add(unis[5])

uczelnie.print_list()

print(uczelnie.length())

uczelnie.remove()

print("Po usunięciu pierwszego elementu:")
print(uczelnie.get())
print(" ")

uczelnie.remove_end()

uczelnie.print_list()

uczelnie.destroy()
print(uczelnie.is_empty())

uczelnie.remove()
uczelnie.remove_end()
uczelnie.add(unis[0])
uczelnie.remove_end()
print(uczelnie.is_empty())  
