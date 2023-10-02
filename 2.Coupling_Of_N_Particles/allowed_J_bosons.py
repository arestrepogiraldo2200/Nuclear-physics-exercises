import numpy as np

print("\n↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
print("This program computes the allowed angular momentum values of N identical bosons in a j-orbital using the m-scheme.")
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n")

N = int(input("Enter the number of bosons in the orbital: "))
j = int(input("Enter the total angular momentum j of the orbital: "))

# Validation of input
while (N > 2*j+1):

    print("\nMore particles tha allowed. It must hold N <= 2j+1. ")

    N = int(input("Enter the number of bosons in the orbital: "))
    j = int(input("Enter the total angular momentum j of the orbital: "))

# Numerators of the allowed projections of j
numerator = []
for a in range(j,-j-1,-1):
    numerator.append(a)

# Allowed projections of total angular momentum
projections = []

# This function calls itself in order to construct the necessary for loops for the calculation
# start: Beggining index of numerators of allowed projections array for the first iteration
# stop: End index of numerators of allowed projections array for the first iteration
# iter: Number of calls to the function
# carry: Sum of numerators of allowed projections

def forfunc(start, stop, iter = 1, carry = 0):

    if (iter <= N):
        for i in range (start, stop):
            forfunc(i, stop, iter+1, carry + numerator[i])
    else:
        projections.append(carry)

forfunc(0, len(numerator))

# Function to extract the J values from the allowed M projections
J = []

def Jvalues():

    removed = 0
    length = len(projections)

    while (removed < length):

        maximum = max(projections)
        J.append(maximum)

        for i in range(maximum, -1*maximum - 1, -1):
            projections.remove(i)
            removed += 1

Jvalues()

# Function to print the results
def result():
    array_result = []
    for i in J:
        array_result.append(str(i))

    print("The allowed total angular momentum values are: ", end = '')
    for i in array_result:
        print(i, "  ", end = '') 
    print("")

result()

