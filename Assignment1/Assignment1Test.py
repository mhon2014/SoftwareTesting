#!/usr/bin/env python3
import sys
import os
import pandas as pd

class object:
    '''Matrix class with functions'''
    def __init__(self):
        try:
            #get size and convert to int
            self.size = int(sys.stdin.readline())+1
            # input = sys.stdin.readlines()
            # print(input)

            '''Matrix initialization'''
            self.matrix = [[0 for i in range(self.size)] for j in range(self.size)]

            for line in sys.stdin.readlines():
                x , y = line.split()
                x = int(x)
                y = int(y)
                self.matrix[x][y] = 1
                self.matrix[0][y] += 1
                self.matrix[x][0] += 1

            pretty = pd.DataFrame(self.matrix)
            #print(pretty)
            print(pretty.drop(0).drop(columns=0))

        except:
            print("Error handling file.\n")

    def onetoone(self):
        '''Check if matrix is one to one counting the number of connections on the domain and range'''
        xCounter = 0
        yCounter = 0

        #check the both the range and domain to make sure they don't have more than 1 connection
        for i in range(1, self.size):
            if(self.matrix[i][0] > 1 or self.matrix[0][i] > 1):
                return False
            
            #count both the domain connection and range connections
            if(self.matrix[0][i] == 1):
                xCounter += 1

            if(self.matrix[i][0] == 1):
                yCounter += 1
        
        #compare both the counters, if they're not the same then it's not one to one
        if(xCounter != yCounter):
            return False

        return True

    def onto(self):
        '''Check if matrix is onto by checking that everything in the range has a connection to at least one in the domain'''
        for i in range(1,self.size):
            if (self.matrix[0][i] < 1):
                return False
        return True

    def reflexive(self):
        '''Check reflexiveness by checking the diagonals in the matrix'''
        for i in range(1, self.size):
            if (self.matrix[i][i] != 1):
                return False
        return True

    def symmetric(self):
        '''Check symmetric'''
        for i in range(1, self.size):
            for j in range(1, i):
                if(not self.matrix[i][j] and not self.matrix[i][j]):
                    return False
        return True

    def transitive(self):
        '''Check transitivity of the output'''
        for a, b in range(1,self.size):
            print(1)
            # print(f"{a}, {b}")
        #     for c, d in self.matrix:
        #         if b == c and ((a, d) not in self.matrix):
        #             return False
        # return True

    def equivalence(self):
        '''Check equivalence'''
        pass

    def function(self):
        '''Check if function by checking that everything in the domain has a unique mapping to the range'''
        for i in range(1, self.size):
            if (self.matrix[i][0] != 1):
                return False
        return True


if __name__ == "__main__":

    #ssh mhon2014@code01.fit.edu '/udrive/faculty/kgallagher/public_html/sampleprogs/onto 15' | ./Assignment1Test.py
    
    testingfunctions = object()

    print(f"One to one: {testingfunctions.onetoone()}")
    print(f"Onto: {testingfunctions.onto()}")
    print(f"Reflexive: {testingfunctions.reflexive()}")
    print(f"Function: {testingfunctions.function()}")
    print(f"Symmetric: {testingfunctions.symmetric()}")
    print(f"Transitive: {testingfunctions.transitive()}")

    
