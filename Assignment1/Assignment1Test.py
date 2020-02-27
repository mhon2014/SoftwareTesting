#!/usr/bin/env python3
import sys
import os
import pandas as pd
from collections import defaultdict

class blackbox:
    '''Matrix class with functions'''
    def __init__(self):
        try:
            #get size and convert to int
            self.size = int(sys.stdin.readline())+1

            self.isOneToOne = False
            self.isOnto = False
            self.isSymmetric = False
            self.isReflexive = False
            self.isTransitive = False
            self.isFunction = False

            # input = sys.stdin.readlines()
            # print(input)

            '''Matrix initialization'''
            self.matrix = [[0 for i in range(self.size)] for j in range(self.size)]

            for line in sys.stdin.readlines():
                x , y = line.split()
                x = int(x)
                y = int(y)
                if(not self.matrix[x][y]):
                    self.matrix[x][y] = 1
                    self.matrix[0][y] += 1
                    self.matrix[x][0] += 1

            #pretty = pd.DataFrame(self.matrix)
            #print(pretty)
            #print(pretty.drop(0).drop(columns=0))

        except:
            print("Error handling file.\n")

    def run(self):
        '''Run the functions and save the states'''
        self.isOneToOne = self.onetoone()
        self.isOnto = self.onto()
        self.isSymmetric = self.symmetric()
        self.isReflexive = self.reflexive()
        self.isTransitive = self.transitive()
        self.isFunction = self.function()
        self.isEquivalence = self.equivalence()


    def printResult(self):
        '''Print result of of the object'''
        print(f"One to one: {self.isOneToOne}")
        print(f"Onto: {self.isOnto}")
        print(f"Reflexive: {self.isReflexive}")
        print(f"Function: {self.isFunction}")
        print(f"Symmetric: {self.isSymmetric}")
        print(f"Transitive: {self.isTransitive}")
        print(f"Equivalence: {self.isEquivalence}")
            #test equivalence
        if(self.isEquivalence):
          self.printpartitions()
    

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
            for j in range(1, i): #could've used exclusive or, symmetric = [a][b] = [b][a]
                # if((self.matrix[i][j] and not self.matrix[j][i]) or (not self.matrix[i][j] and self.matrix[j][i])):
                if(self.matrix[i][j] ^ self.matrix[j][i]):
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
        '''Check equivalence by checking if reflexive, symmetric and transitive'''
        #variable to save the states
        if not (self.isReflexive and self.isSymmetric and self.isTransitive):
            return False
        return True

    def printpartitions(self):
        '''Print partitions'''

        #Fix the datastructure list or use 1 array
        usedset = [False for i in range(1,self.size)] #list for usedset so it doesn't repeat in the set list

        hashlist = defaultdict(list) #sets

        counter = 0 #counter to count partitions

        for i in range(1,self.size):
            for j in range(1,self.size):
                if(self.matrix[i][j] and not usedset[j-1]): #if indice is not in the used set
                    usedset[j-1] = True #append it
                    hashlist[i].append(j)

        if (len(hashlist) < 25): #if there's less than 10 partitions, print it out
            for key in hashlist:
                print(f"{hashlist[key]}")
        
        print(f"Partitions: {len(hashlist)}")
                
    def function(self):
        '''Check if function by checking that everything in the domain has a unique mapping to the range'''
        for i in range(1, self.size):
            if (self.matrix[i][0] != 1):
                return False
        return True


if __name__ == "__main__":

    #ignore these comments
    #ssh mhon2014@code01.fit.edu '/udrive/faculty/kgallagher/public_html/sampleprogs/executable | ./Assignment1Test.py
    #code01 '/udrive/faculty/kgallagher/public_html/sampleprogs/sym 10' | ./Assignment1Test.py
    
    #create the object
    testingfunctions = blackbox()

    #run the object
    testingfunctions.run()

    #print out the result
    testingfunctions.printResult()

