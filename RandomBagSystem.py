#!/usr/bin/python
import sys
import random
from array import *

def TetrominoPiece():
    x = 0
    result = ''
    while(x<50):
        Tetrominos = array('u',['O','I','S','Z','L','J','T'])
        for i in range(0,7): 
            randomTetromino = random.choice(Tetrominos) 
            Tetrominos.remove(randomTetromino)
            result += randomTetromino
        x = x + 1
    print(result)
    return result
TetrominoPiece()
