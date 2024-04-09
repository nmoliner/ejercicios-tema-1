lista_1 = ["h", 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
lista_2 = ["h", 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a']

# Find the common elements between the two lists
common_elements = list(set(lista_1) & set(lista_2))

# Create a new list without any duplicates
new_list = list(set(common_elements))

print(new_list)

