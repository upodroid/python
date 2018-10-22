# Q1 sort these and print out the largest

numbersQ1 = [123, 354, 324, 2340, 324, 243, 756, 955]
numbersf = {int(x) for x in numbersQ1}
# numbers.sort()

print(sorted(numbersQ1))  # sorts numbers
final = sorted(numbersQ1)

print((final[-1]), "is the biggest number in array")
print()


# ## Q2
numbersQ2 = [432, 435, "588", "463", 234]
Q2int = [int(x) for x in numbersQ2] # convert to int
Q2str = [str(x) for x in numbersQ2] # convert to str
print(Q2int)
print(Q2str)
print()

# Q3

pairValue = {"K1": "V1", "K2": "V2", "K3": "V3"}
print(pairValue)
fpair = {val:key for (key,val) in pairValue.items()}
print(fpair)

# Q4
q4 = (1, 2, 3, 4, 5)
print(q4)

# Q5

resultsq5 = [50, 96, 45, 67, 88]
Q5ans = sum(i < 70 for i in resultsq5)
print( "There are ", Q5ans, " failed exams")
print()


# 6

q6 = [33, 56, 75, 78, 34, 56]
for i in range(0,5):
    if (q6[i] % 3 == 0) and (q6[i] % 5 == 0):
        print( q6[i],"fizzbuzz")
    elif q6[i] % 5 == 0:
            print( q6[i],"buzz")
    elif q6[i] % 3 == 0:
            print( q6[i],"fizz")

