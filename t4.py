from turtle import *
speed('fastest')
i=1
while True:
    fd(10 + i)
    lt(360/3)
    i += 2
    if i > 1000:
        break