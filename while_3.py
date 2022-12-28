total=0
while True:
    num= input("Enter a number")
    if not num:
        break
    if num.isnumeric():
        total += int(num)
    print(f"total => {total}")
