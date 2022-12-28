elements = ["Hydrogen","Helium","Lithium"]

print(elements)
print('Individual elements:')
print(elements[0])
print(elements[1])
print(elements[2])

# changing a list element (mutability)
elements[1] = "Carbon"
print(elements)

print(elements, elements , elements, sep="\n")

elements.insert(1,'Chlorine')
elements.insert(100,'Nitrogen')
elements.insert(3,'Oxygen')
print(elements)

nobel_metals = ['Gold','Silver','Platinum']
elements.extend(nobel_metals) # adds multiple elements to the end of the list
print(elements)
elements.append(nobel_metals)
print(elements)