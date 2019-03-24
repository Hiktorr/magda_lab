#task 1
#calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
for x in range(56,101):
    y = 2*x**2 + 2*x + 2
    print(y)

#task 2
#ask the user for a number and print its factorial (1p)
inputNumber = int(input("Input the number\n"))
result = 1
for i in range(1,inputNumber +1):
    result = result * i
print("The factorial of {} is {}".format(inputNumber, result))

#task 3
#write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
def lowestElementOfArray(arr):
    min_value = min(arr)
    index = []
    for i in range(len(arr)):
        if arr[i] == min_value:
            index.append(i)
    return index, min(arr)


inputArray = [10, 20, 3, 30 , 5, 4, 3]
print("The lowest element of array is {} and index of that element is {}".format(lowestElementOfArray(inputArray)[1],lowestElementOfArray(inputArray)[0]))

