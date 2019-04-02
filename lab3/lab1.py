#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)
#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
#3 Test your solutions

from math import pi

def countField(figureType, x = None, y = None):
    figureType = str(figureType).lower()
    if figureType == "circle":
        if x == None:
            print("You need to enter valid radius length")
            exit()
        if x < 0:
            print("Radius cannot be lower than 0")
            exit()
        return pi * pow(x,2)
    elif figureType == "rectangle":
        if x == None or y == None:
            print("You need to enter valid side length")
            exit()
        if x < 0 or y < 0:
            print("Sides of the rectangle cannot be lower than 0")
            exit()
        return x * y
    elif figureType == "triangle":
        if x == None or y == None:
            print("You need to enter valid base or height length")
            exit()
        if x < 0 or y < 0:
            print("Height or base cannot be lower than 0")
            exit()
        return 0.5 * x * y
    elif figureType == "rhombus":
        if x == None or y == None:
            print("You need to enter valid diagonal length")
            exit()
        if x < 0 or y < 0:
            print("Diagonals cannot be lower than 0")
            exit()
        return 0.5 * x * y
    else:
        print("You don't pass valid figure name")

def compareFields(fig1 = [], fig2 = []):

    if len(fig1) < 3:
        for i in range(3-len(fig1)):
            fig1.append(None)
    elif len(fig1) > 3:
        print("Too many arguments")
        exit()
    if len(fig2) < 3:
        for i in range(3-len(fig2)):
            fig2.append(None)
    elif len(fig2) > 3:
        print("Too many arguments")
        exit()

    fig1Field = countField(fig1[0], fig1[1], fig1[2])
    fig2Field = countField(fig2[0], fig2[1], fig2[2])
    # print(fig1Field, fig2Field)
    if fig1Field and fig2Field is not None:
        if fig1Field > fig2Field:
            print(f"The first figure ({fig1[0]}) has larger field")
        elif fig2Field > fig1Field:
            print(f"The second figure ({fig2[0]}) has larger field")
        elif fig2Field == fig1Field:
            print(f"The figures ({fig1[0]}, {fig2[0]}) has equal field")
    else:
        print("You pass the wrong input")

# print(countField("rhombus",5,5))
compareFields(['circle',5,3],['circle', 10, 3])