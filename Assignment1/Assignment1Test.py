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
                if((self.matrix[i][j] and not self.matrix[j][i]) or (not self.matrix[i][j] and self.matrix[j][i])):
                    return False
        return True

    def transitive(self):
        '''Check transitivity of the program using indices'''
        for a in range(1,self.size):
            for b in range(1, self.size):
                if (not self.matrix[a][b]): #A & B  skip indices that are 0
                    continue

                for c in range(1,self.size):
                    if(not self.matrix[b][c]): # B & C skip indices that are 0
                        continue

                    if (not self.matrix[a][c]):  # A & C
                        return False

        return True

    def equivalence(self):
        '''Check equivalence'''
        if not (self.reflexive() and self.symmetric() and self.transitive()):
            return False
        return True

    def printpartitions(self):
        '''Print partitions'''
        usedset = []

        setlist = [set() for i in range(1, self.size)]

        counter = 0 #counter to count partitions

        for i in range(1,self.size):
            for j in range(1,self.size):
                if(self.matrix[i][j] and j not in usedset): #if indice is not in the 
                    counter += 1
                    usedset.append(j)
                    setlist[i-1].add(j)

        if (counter < 10): #if there's less than 10 partitions, print it out
            for i in range(1,self.size):
                if(len(setlist[i-1]) != 0):
                    print(f"{i} {setlist[i-1]}")
        
        print(f"Partitions: {counter}")
                
    def function(self):
        '''Check if function by checking that everything in the domain has a unique mapping to the range'''
        for i in range(1, self.size):
            if (self.matrix[i][0] != 1):
                return False
        return True


if __name__ == "__main__":

    #ssh mhon2014@code01.fit.edu '/udrive/faculty/kgallagher/public_html/sampleprogs/executable | ./Assignment1Test.py
    
    testingfunctions = object()

    print(f"One to one: {testingfunctions.onetoone()}")
    print(f"Onto: {testingfunctions.onto()}")
    print(f"Reflexive: {testingfunctions.reflexive()}")
    print(f"Function: {testingfunctions.function()}")
    print(f"Symmetric: {testingfunctions.symmetric()}")
    print(f"Transitive: {testingfunctions.transitive()}")
    print(f"Equivalence: {testingfunctions.equivalence()}")

    if(testingfunctions.equivalence()):
        testingfunctions.printpartitions()
    
