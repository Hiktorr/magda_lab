from cs50 import get_int
from math import pi
x = -1
y = -1
while not x>=0:
    x = get_int("Input circle X radius: ")
while not y>=0:
    y = get_int("Input circle Y radius: ")

print("Circle X")
print(f"Perimeter = {2*pi*x} | Field = {pi*pow(x,2)}")

print("Circle Y")
print(f"Perimeter = {2*pi*y} | Field = {pi*pow(y,2)}")
