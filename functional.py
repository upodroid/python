from functools import partial

def sumOf(a, b):
    return(a + b)

print (sumOf(1, 2))

# partial

plusTwo = partial (sumOf, 2)
print (plusTwo)

