#hello_world_genetic_249.py

#Reddit Daily Programmer Challenge #249 (Intermediate), Hello World Genetic or Evolutionary Algorithm

#Problemset found here: https://www.reddit.com/r/dailyprogrammer/comments/40rs67/20160113_challenge_249_intermediate_hello_world/

import random
import string

target = input("Enter target to evolve towards: ")
pool = string.printable #Pool of ascii characters to select from 
#Using Hamming Distance as a measure of genetic fitness
def hamming_distance(str1, str2):
    count = 0
    for i, x in zip(str1, str2):
        if i == x:
            continue
        else:
            count += 1
    return int(count)
    
def random_string_gen(target):
    creature = "".join(random.sample(pool, len(target)))
    return creature

#Using a basic genetic algorithm for fitness measurement
def genetic_algorithm():
    generation = 0
    max_generation = 100
    inp = list(target)
    rand = list(random_string_gen(target)) #Initialization
    while inp != rand:
        for n in range(len(inp)):
            if inp[n] != rand[n]:
                rand[n] = random.choice(pool)
                ham_dist = hamming_distance(target, "".join(rand))
                print("Gen", generation, "|", "Fitness", ham_dist, "|", "".join(rand))
                generation += 1
           # if generation == max_generation: 
           #    break
            
genetic_algorithm()
