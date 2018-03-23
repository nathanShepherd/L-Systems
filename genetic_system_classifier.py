# (Probabilistic) Genetic L-System

'''
Darwinian Natural Selection
--> Variation: There is a variety of traits and or a means of mutation
--> Selection: Threshold of fitness for specific traits
--> Heredity: Children recieve parent's genetic information

X = str()# Features
Y = str()# Labels

Genetic Algorithm
1.) Create a random population of N genetic objects
     ex.) Predict "cat" from (tar, aat, ase, etc.)

2.) Calculate Fitness for all N elements

3.) Selection of M genetic objects
     ex.) Assign probability of selecting each object relative to Fitness
     ex.) Probability of selection for cat >> tar == .33, aas == .66, ase == .01

4.) Reproduction via some means
     ex.) tar + aas >> t|ar + a|as >> (probablilistic mutation) >> tas (del ase)
'''

#class or array --> Population
#class DNA --> creates genetic objects

import numpy as np
import random
import math
class DNA():
    def __init__(self, in_data, target):
        #funct Fitness(optimization)
        #how to encode DNA
        #   --> Genetype(data <-- funct(encoding))
        #   --> Phenotype(expression of DNA, viz)
        self.target = target
        self.in_data = in_data
        # array == delta matrix
        self.array = [random.randint(0, 1) for i in range(len(target))]
        self.reject = False
        self.calc_fitness()
        self.mating_index = None

    def calc_fitness(self):
        self.fitness = 0
        self.delta_matrix = []
        for i, dim in enumerate(self.array):
            if char == self.target[i]:
                self.fitness += 1
        self.fitness = np.exp(self.fitness)

    def reproduce(self, population):
        # use population.mating_index
        #combine DNA in a meaningful way
        child_dna = self.array
        for i in range(len(self.array)):
            if self.array[i] == self.target[i]:
                child_dna[i] = self.array[i]
                
            elif population[self.mating_index].array[i] == self.target[i]:
                child_dna[i] = population[self.mating_index].array[i]
                
            else:
                child_dna[i] = self.alpha[random.randint(0, len(self.alpha) - 1)]
                
        self.array = child_dna
        

class Population():
    def __init__(self, size, in_data, target):
        self.arr = []
        self.target = target
        for i in range(size):
            random_variable = DNA(in_data, target)
            self.arr.append(random_variable)

    def fittest_of(self):
        #determine acc of neural network
        maximal = 0
        for dna in self.arr:
            if dna.fitness > maximal:
                maximal = dna.fitness
        return maximal

    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))

    def selection(self):
        #select for dna that is closest to target after dot product
        for i, dna in enumerate(self.arr):
            #parent_index == i
            #if np.random.normal(2/3, 1/3) < adjusted_sigmoid(dna.fitness/fittest_of(population)):
            if random.randint(0,1) < self.sigmoid(dna.fitness/self.fittest_of()) or len(dna.array) > len(dna.target):
                dna.reject = True
            else:
                dna.reject = False
                dna.mating_index = math.floor(random.randint(0, len(self.arr)-1))

        for dna in self.arr:
            if not dna.reject:
                dna.reproduce(self.arr)

    def evolve(self):
        generation = 0
        while self.fittest_of() < len(self.target):
            self.selection()
            generation += 1
            fittest = self.fittest_of()
            best_string = ""
            printed = False
            for dna in self.arr:
                if dna.fitness == fittest and not printed:
                    for char in dna.array:
                        best_string += char
                    printed = True
            acc = 0
            for i, char in enumerate(best_string):
                if char == self.target[i]:
                    acc += 1
            print('Generation: {} || Accuracy: {} || Best String: {}'.format(generation, acc*100//len(self.target), best_string))
            if best_string == self.target:
                print("\nEvolved to target phenotype")
                break
        

def main():
    # Reached target of 155 characters in 102 generations (2 seconds)
    target = [0, 0, 1]
    in_data = [5, 8, 3, 2, 1, -9, -3, 2]

    clf = Population(50, in_data, target)
    clf.evolve()
    
    
main()
    



















