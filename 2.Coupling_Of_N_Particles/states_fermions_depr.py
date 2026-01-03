import numpy as np
from collections import Counter

print("\n↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓")
print("This program computes the allowed angular momentum values of N identical fermions in k j-orbitals using the m-scheme.")
print("↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓\n")

N  = int(input("Enter the number of fermions in the orbital: "))
nj = int(input("Enter the number k of j-orbitals: "))
j  = []

for i in range(nj):
    
    inpt_j = str(input("Enter the total angular momentum j_"+str(i+1)+" in format a/b: "))
    ja = int(inpt_j.split("/")[0])
    jb = int(inpt_j.split("/")[1])
    
    # Validation of input
    while (jb != 2 or ja%2 == 0):

        if (jb != 2 or ja%2 == 0):
            print("\nj must be half-integer. ")
            
        inpt_j = str(input("Enter the total angular momentum j_"+str(i+1)+" in format a/b: "))
        ja = int(inpt_j.split("/")[0])
        jb = int(inpt_j.split("/")[1])
    
    j.append(inpt_j)
          
# Numerators
ja  = [int(n.split("/")[0]) for n in j]

# Array of maximum particles per state
deg = [ja_j+1 for ja_j in ja]

# Validation of degeneracies input
if N > sum(deg):
    print("Larger number of particles ("+str(N)+") than degeneracies of orbitals entered ("+str(sum(deg))+"). Program finished.")
    quit()

# Total angular momentum of the state
I = int(input("Enter a value of total angular momentum I or type -1 to print all possible couplings: "))


# Configurations. Generated partially with chatGPT5 ===================================================== 
def configurations(N, k):
    
    solutions = []

    def backtrack(remaining, variables, current):
        if variables == 1:
            solutions.append(current + [remaining])
            return
        for i in range(remaining + 1):
            backtrack(remaining - i, variables - 1, current + [i])
    backtrack(N, k, [])
    
    # Solutions that hold multiplicities
    valid_sols = []
    
    for sols in solutions:
        
        flag = False
        
        for i in range(k):
            if sols[i] > deg[i]:
                flag = True
                break
        if flag:
            continue
        else:
            valid_sols.append(sols)     

    return valid_sols

# Function to calculate N particles in orbital j =====================================================
def single_j_couplings(ja, N):

    # Numerators of the allowed projections of j
    numerator = []
    for a in range(ja,-ja-1,-2):
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
                forfunc(i+1, stop+1, iter+1, carry + numerator[i])
        else:
            projections.append(carry)

    forfunc(0, len(numerator)- N +1)

    # Function to extract the J values from the allowed M projections
    J = []

    def Jvalues():

        removed = 0
        length = len(projections)

        while (removed < length):

            maximum = max(projections)
            J.append(maximum)

            for i in range(maximum, -1*maximum - 1, -2):
                projections.remove(i)
                removed += 1

    Jvalues()

    # Function to print the results
    def result():
        array_result = []
        for i in J:
            array_result.append(str(int(i/2)) if i%2==0 else str(i)+"/2")

        array_result_mult = [[item, count] for item, count in Counter(array_result).items()]

        return array_result_mult

    rr = result()
    
    return rr
# ======================================================================================================

# Converts format "a/b" to floating ====================================================================
def format_converter(s):
    return float(s.split("/")[0])/2
    
# ======================================================================================================

# Converts format "a/b" to floating ====================================================================
def inverse_format_converter(f):
    if f%1==0:
        return str(int(f))
    else:
        return str(int(2*f))+"/2"
    
# ======================================================================================================

# Possible couplings ===================================================================================
def jj_coupling(ja, jb):
    return [j for j in np.arange(abs(ja-jb), ja+jb+1)]
    
# ======================================================================================================


# Calculate all allowed configurations
confs = configurations(N,nj)

# List to store the couplings of same-j particles in the allowed configurations
coupl = []

# Calculation of allowed couplings of individual orbitals
for conf in confs:
    
    cc = []
    
    for i in range(nj):
        cc.append(single_j_couplings(ja[i], conf[i]))
            
    coupl.append(cc)
    
# ======================================================================================================
# Table header
space = "\t\t"
print("\n")
for i in range(nj):
    
    if i ==0:
        print(str("n{0}"+space+"j{0}^m{0}"+space).format(str(i+1)), end="")
        co_in = str(i+1)
    
    if i >= 1:
        co_in += str(i+1)
        print(str("n{0}"+space+"j{0}^m{0}"+space+"j{1}"+space).format(str(i+1),co_in), end="")
print("\n")
for i in range(nj):
    
    if i ==0:
        print("_______________________________", end="")
    
    if i >= 1:
        print("________________________________________________", end="")
print("\n")    
    
# ======================================================================================================


for i in range(len(confs)):                           # Loop over configurations
    
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     print("Conf:", confs[i])
    
    for j in range(len(coupl[i][0])):                    # Loop over couplings of j1
        for k in range(len(coupl[i][1])):                # Loop over couplings of j2
            
            j1 = format_converter(coupl[i][0][j][0]) if "/" in coupl[i][0][j][0] else float(coupl[i][0][j][0])
            j2 = format_converter(coupl[i][1][k][0]) if "/" in coupl[i][1][k][0] else float(coupl[i][1][k][0])

            j12_list = jj_coupling(j1, j2)
#             print(j1,"x",j2,"=",j12_list)

            
            for l in range(len(j12_list)):
                for m in range(len(coupl[i][2])):
                    
                    j12 = j12_list[l]
                    j3  = format_converter(coupl[i][2][m][0]) if "/" in coupl[i][2][m][0] else float(coupl[i][2][m][0])
                    
                    j123_list = jj_coupling(j12, j3)
                    
#                     print("######################")                    
#                     print(j12,"x",j3,"=",j123_list)

                    for n in range(len(j123_list)):
        
                        if I == -1:
                            print(str(confs[i][0])+space+inverse_format_converter(j1)+"^"+str(coupl[i][0][j][1])+space+
                                  str(confs[i][1])+space+inverse_format_converter(j2)+"^"+str(coupl[i][1][k][1])+space+
                                  "||"+inverse_format_converter(j12)+"||"+space+
                                  str(confs[i][2])+space+inverse_format_converter(j3)+"^"+str(coupl[i][2][m][1])+space+
                                  "||"+inverse_format_converter(j123_list[n])+"||")

                        else:
                            
                            if j123_list[n] == I:

                                print(str(confs[i][0])+space+inverse_format_converter(j1)+"^"+str(coupl[i][0][j][1])+space+
                                      str(confs[i][1])+space+inverse_format_converter(j2)+"^"+str(coupl[i][1][k][1])+space+
                                      "||"+inverse_format_converter(j12)+"||"+space+
                                      str(confs[i][2])+space+inverse_format_converter(j3)+"^"+str(coupl[i][2][m][1])+space+
                                      "||"+inverse_format_converter(j123_list[n])+"||")


                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
        
        
        
        
        
        
        
        
    
    
    # print(confs)
    
# ######################################
# for ss in coupl:
#     print(ss)
# ######################################
# print("============================")

 
    
    
    
    
    
    
    

