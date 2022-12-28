fruits = ['Apple', 'Banana', 'Orange', 'Pear', 'Grape']
dry_fruits = ['Almond', 'Cashew', 'Pistachio', 'Walnut']

print(fruits,len(fruits))
fruits.extend(dry_fruits)
print(fruits, len(fruits))

fruits.remove('Apple') # removes element by value
# fruits.remove('Orange')
# fruits.remove('Grape')

fruits.pop(3) # remove element by index
fruits.pop() # remove last element (default)
print(fruits)

fruits.reverse()
print(fruits)

# total 11 functions in list
# 1. append, 2. insert
# 3. extend, 4. remove
# 5. pop, 6. clear
# 7. index, 8. count
# 9. sort, 10. reverse
# 11. copy