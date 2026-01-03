import numpy as np
from collections import Counter

print("\n↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓")
print("This program computes the allowed angular momentum values of N identical fermions in k j-orbitals using the m-scheme.")
print("↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓↑↓\n")

N  = int(input("Enter the number of fermions in the orbital: "))
nj = int(input("Enter the number k of j-orbitals: "))
j  = []

for i in range(nj):
    
    inpt_j = str(input("Enter the total angular momentum j"+str(i+1)+" in format a/b: "))
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
I = str(input("Enter a value of total angular momentum I or type -1 to print all possible couplings: "))

if "/" in I:
    I = float(I.split("/")[0])/2
else:
    I = int(I)
    
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

# Recursive function to couple lists of angular momentum
def coupler_of_coupled(ja_list, conf_index, index_nj, row):
    
    if index_nj <= nj-2:
        
#         THERE IS AN UNRESOLVED BYG IN THE PRINTING FOR MORE THAN 3 ANGULAR MOMENTUM STATES !!!!!!!!!!!!!!!!!!!!!
#         CALCULATIONS ARE OK BUT THE PRINTING REPEATS BECAUSE IT CONCATENATES

        for i in range(len(ja_list)):
            for j in range(len(coupl[conf_index][index_nj])):

                ja = ja_list[i]
                jb = format_converter(coupl[conf_index][index_nj][j][0]) if "/" in coupl[conf_index][index_nj][j][0] else                                                                                        float(coupl[conf_index][index_nj][j][0])
                
                row_new = (row
                    + "||" + inverse_format_converter(ja)
                    + "||" + space
                    + str(confs[conf_index][index_nj]) + space
                    + inverse_format_converter(jb)
                    + "^" + str(coupl[conf_index][index_nj][j][1]) + space)
                
                jab_list = jj_coupling(ja, jb)

                coupler_of_coupled(jab_list, conf_index, index_nj+1, row_new)
                
    else:
        for i in range(len(ja_list)):
            for j in range(len(coupl[conf_index][index_nj])):

                ja = ja_list[i]
                jb = format_converter(coupl[conf_index][index_nj][j][0]) if "/" in coupl[conf_index][index_nj][j][0] else                                                                                        float(coupl[conf_index][index_nj][j][0])
                
                row_temp = "||"+inverse_format_converter(ja)+"||"+space+str(confs[conf_index][index_nj])+space+                                                 inverse_format_converter(jb)+"^"+str(coupl[conf_index][index_nj][j][1])+space
                jab_list = jj_coupling(ja, jb)
                                
                for n in range(len(jab_list)):

                    if I == -1:
                        print(row+row_temp+"||"+inverse_format_converter(jab_list[n])+"||"+space+"\n")                    
                    else:
                        if jab_list[n] == I:
                            print(row+row_temp+"||"+inverse_format_converter(jab_list[n])+"||"+space+"\n")

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
    
    # Case of a single j-orbital
    if nj == 1:
        for j in range(len(coupl[i][0])):                    # Loop over couplings of j1
            j1 = format_converter(coupl[i][0][j][0]) if "/" in coupl[i][0][j][0] else float(coupl[i][0][j][0])
            
            if I == -1:
                print(str(confs[i][0])+space+inverse_format_converter(j1)+"^"+str(coupl[i][0][j][1]))
            else:
                if j1 == I:
                    print(str(confs[i][0])+space+inverse_format_converter(j1)+"^"+str(coupl[i][0][j][1]))


    # Case of more than one j-orbitals
    else:
        
        row = ""

        # Initial case of first two j-orbitals
        for j in range(len(coupl[i][0])):                    # Loop over couplings of j1
            for k in range(len(coupl[i][1])):                # Loop over couplings of j2

                j1 = format_converter(coupl[i][0][j][0]) if "/" in coupl[i][0][j][0] else float(coupl[i][0][j][0])
                j2 = format_converter(coupl[i][1][k][0]) if "/" in coupl[i][1][k][0] else float(coupl[i][1][k][0])

                j12_list = jj_coupling(j1, j2)
                
                if nj > 2:
                    # Couples the j12 to j3, then j123 to j4 and so on. This is an essential step in this code.
                    
                    r1 = str(confs[i][0])+space+inverse_format_converter(j1)+"^"+str(coupl[i][0][j][1])+space
                    r2 = str(confs[i][1])+space+inverse_format_converter(j2)+"^"+str(coupl[i][1][k][1])+space
                    row = r1+r2
                    
                    coupler_of_coupled(j12_list, i, 2, row)
                    
                else:
                    # Printing of table in the case of only two j-orbitals
                    for n in range(len(j12_list)):

                        if I == -1:
                            for l in range(nj):
                                if l == 0:
                                    print(str(confs[i][l])+space+inverse_format_converter(j1)+"^"+str(coupl[i][0][j][1])+space,                                                                                                                         end="")
                                if l >= 1:
                                    print(str(confs[i][l])+space+inverse_format_converter(j2)+"^"+str(coupl[i][1][k][1])+space+
                                                                      "||"+inverse_format_converter(j12_list[n])+"||", end="")
                                    print("\n")
                                
                        else:
                            if j12_list[n] == I:                
                                for l in range(nj):
                                    if l == 0:
                                        print(str(confs[i][l])+space+inverse_format_converter(j1)+"^"+str(coupl[i][0][j]                                                                                                                     [1])+space,                                                                                                                         end="")
                                    if l >= 1:
                                        print(str(confs[i][l])+space+inverse_format_converter(j2)+"^"+str(coupl[i][1][k]                                                                                                                    [1])+space+
                                                                          "||"+inverse_format_converter(j12_list[n])+"||",                                                                                                                        end="")
                                        print("\n")                
                                        