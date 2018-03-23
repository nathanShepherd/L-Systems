# (Probabilistic) Genetic L-System

def apply_rules(char):
    '''
    Example 7: Fractal plant[edit]
    variables : X F
    constants : + − [ ]
    start  : X
    rules  : (X → F[−X][X]F[−X]+FX), (F → FF)
    angle  : 25°
    '''
    if char ==  "F":
        return 'F-F+B+F-F'
    elif char == "B":
        return 'F-F++F-F'
    else:
        return char

def gen_str(axiom, iters):
    delta = axiom
    for i in range(iters):
        new_str = ""
        for char in delta:
            new_str += apply_rules(char)
        delta = new_str
    return delta

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
    alpha = 'abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'+' (@).!?><:*=_/,\\'+'1234567890'
    def __init__(self, target):
        #funct Fitness(optimization)
        #how to encode DNA
        #   --> Genetype(data <-- funct(encoding))
        #   --> Phenotype(expression of DNA, viz)
        self.target = target
        self.array = [self.alpha[random.randint(0, len(self.alpha) - 1)] for i in range(len(target))]
        self.reject = False
        self.calc_fitness()
        self.mating_index = None

    def calc_fitness(self):
        self.fitness = 0
        #exponentiate fitness function
        for i, char in enumerate(self.array):
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
        

population = []
def init_population(size, target):
    for i in range(size):
        random_variable = DNA(target)
        population.append(random_variable)

def fittest_of(all_members):
    maximal = 0
    for dna in all_members:
        if dna.fitness > maximal:
            maximal = dna.fitness
    return maximal

def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

def selection():
    # --> floor(random(0,3))
    for i, dna in enumerate(population):
        #parent_index == i
        #if np.random.normal(2/3, 1/3) < adjusted_sigmoid(dna.fitness/fittest_of(population)):
        if random.randint(0,1) < sigmoid(dna.fitness/fittest_of(population)) or len(dna.array) > len(dna.target):
            dna.reject = True
        else:
            dna.reject = False
            dna.mating_index = math.floor(random.randint(0, len(population)-1))

    for dna in population:
        if not dna.reject:
            dna.reproduce(population)

def main():
    # Reached target of 155 characters in 102 generations (2 seconds)
    target = 'Hello there, what is your name?'

    init_population(50, target)

    generation = 0
    while fittest_of(population) < len(target):
        selection()
        generation += 1
        fittest = fittest_of(population)
        best_string = ""
        printed = False
        for dna in population:
            if dna.fitness == fittest_of(population) and not printed:
                for char in dna.array:
                    best_string += char
                printed = True
        acc = 0
        for i, char in enumerate(best_string):
            if char == target[i]:
                acc += 1
        print('Generation: {} || Accuracy: {} || Best String: {}'.format(generation, acc*100/len(target), best_string))
        if best_string == target:
            print("\nEvolved to target phenotype")
            break
    
main()
    



















