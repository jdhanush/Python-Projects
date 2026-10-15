from random import choice

my_words = ["Python", "Code", "PyQt", "Test", "GUI", "App", "Module", "Framework", "Class", "Widget", "Window", "Pushbutton"]

print(choice(my_words))


import numpy as np

x = np.array([["7", "8", "9", "/"],["4", "5", "6", "*"],["1", "2", "3", "-"],["0", ".", "=", "+"]])

for r in range(x.shape[0]):
    for c in range(x.shape[1]):
        print(x[r][c])