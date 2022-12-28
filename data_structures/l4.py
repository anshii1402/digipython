# wap to add 10 numbers in a list by user input

num = []            # blank list
for i in range(10):
    data = input("Enter a number: ")
    if data.isnumeric():
        num.append(int(data))

print("your data => ",num)