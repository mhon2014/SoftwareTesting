#!/usr/bin/env python3
#bullshit test
import sys
import os
import pandas as pd

class object:
    def __init__(self):
        try:
            self.size = int(sys.stdin.readline())+1
            # input = sys.stdin.readlines()
            # print(input)
            self.xDomain = {new_list: [] for new_list in range(1, self.size)}

            self.yDomain = {new_list: [] for new_list in range(1, self.size)}

            for line in sys.stdin.readlines():
                x , y = line.split()
                x = int(x)
                y = int(y)
                self.xDomain[x].append(y)
                self.yDomain[y].append(x)
        except:
            print("Error handling file.\n")

    def onetooneTest(self):
    flag = True
    xCounter = 0
    yCounter = 0

    for i in range(1, self.size):
        if(len(self.xDomain[i]) > 1 or len(self.yDomain[i]) > 1):
            flag = False
            break

        if(len(self.xDomain[i]) == 1):
            xCounter += 1

        if(len(self.yDomain[i]) == 1):
            yCounter += 1

    if(xCounter != yCounter):
        flag = False

    return flag


    def ontoTest(self):
    for i in range(1, self.size):
        if (len(self.yDomain[i]) != 1):
            return False
    return True


    def reflexiveTest(self):
    for i in range(1, self.size):
        if (self.xDomain[i].count(i) < 1):
            return False
    return True

    def functionTest(self):
    for i in range(1, self.size):
        if (len(self.xDomain[i]) != 1):
            return False

    return True


