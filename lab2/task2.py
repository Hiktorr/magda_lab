from cs50 import get_int
inRange = -1
while not inRange>0:
    inRange = get_int("Input find range [ONLY INPUTS GREATER THAN 0]: ")

for x in range(1,inRange+1):
    for y in range(1,x+1):
        if x%y == 0 and not x%2 and not y%2:
            print("{} is divisible by {} and both are even".format(x,y))