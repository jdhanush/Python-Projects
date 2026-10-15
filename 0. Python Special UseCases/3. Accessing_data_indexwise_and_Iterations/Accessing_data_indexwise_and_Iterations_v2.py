import numpy.random as rd
import numpy as np

a = rd.rand(3, 2, 5)

print(f"Stack of matrices: \n{a}")

print("\n")
for iteration, layer in enumerate(a):
    print(f"\nFor i={iteration} matirix of type {type(layer)}: \n{layer}")