#from random import choice
import random as rd

capital = "Topeka"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the range"

def randomfunfact():
    funfacts = [
        "Kansas is considered flat",
        "Wichita is the largest city",
        "Big portion of Kansas is Missouri",
        "Most Kansasans are annoyed"
        ]
    
    index = rd.choice("0123")
    
    print(funfacts[int(index)])