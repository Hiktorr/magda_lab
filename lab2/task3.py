from cs50 import get_float
x = get_float("Input X: ")
y = get_float("Input Y: ")
print(f"{x} is divisible by {y}" if x%y==0 else f"{x} is not divisible by {y}")
