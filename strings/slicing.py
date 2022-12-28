m = "Journey Before Destination"
print(len(m))
for i,v in enumerate(m):
    print(f'{i} --> {v}')

# slicing
print(m[:7])
print(m[8:14])
print(m[-11:])

amt = '$3000'
print(int(amt[1:]))

rr ='1,143 ratings | 452 answered questions'
print("total answers", rr[15:])
print("no of rating", rr[:12])

