"""
This file here is the test file for Git perpouses
"""

import random
def main():
    n = 100
    c = 0
    for i in range(100):
        X=random.randint(0,1000)/1000.0
        Y=random.randint(0,1000)/1000.0
        if X*X+Y*Y <= 1:
            c=c+1
    print(str(4.0*c/n))


main()