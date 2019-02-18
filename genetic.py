from random import randint, uniform
import numpy as np


def inverse_mutation(sequence):
    # Inverts slice between start and end
    jobs = len(sequence)
    # Generating start and end indices randomly
    start = randint(0, jobs - 2)
    end = randint(start + 1, jobs - 1)

    sequence[start:end] = np.fliplr([sequence[start:end]])[0]

    return sequence


def pairwise_swap_mutation(sequence):
    # Swaps start and end positions
    jobs = len(sequence)
    # Generating start and end indices randomly
    start = randint(0, jobs - 2)
    end = randint(start + 1, jobs - 1)

    sequence[start], sequence[end] = sequence[end], sequence[start]

    return sequence


def ordered_crossover(parent1, parent2):
    jobs = len(parent1)
    # Generating start and end indices randomly
    start = randint(0, jobs - 2)
    end = randint(start + 1, jobs - 1)

    # Initialize child list
    child = [-1] * jobs

    # Copy the alleles between start-end from parent1
    child[start:end + 1] = parent1[start:end + 1]

    # Start from 2nd crossover point and
    # copy the rest of the elements in order, cyclically
    parent_index = (end + 1) % jobs
    child_index = (end + 1) % jobs
    while child_index != start:
        if parent2[parent_index] not in child:
            child[child_index] = parent2[parent_index]
            child_index = (child_index + 1) % jobs
        parent_index = (parent_index + 1) % jobs

    return child


def roulette_wheel(sequence, makespan):
    # Store inverses of makespan values in a list
    inverse = []
    for i in makespan:
        j = 1 / i
        inverse.append(j)

    total_sum = 0
    # Calculating sum of all the inverted values
    for i in inverse:
        total_sum = total_sum + i

    # Generate arrays of newsize = 3 * previous size, according to RWS
    newsize = 3 * len(makespan)
    seq = np.ndarray((newsize, sequence.shape[1]))
    mks = np.empty(newsize)

    # Generate 'newsize' number of sequences
    for r in range(newsize):
        # Generating random value between 0 and total_sum
        x = uniform(0, total_sum)
        partial_sum = 0

        for i in range(len(inverse)):
            partial_sum = partial_sum + inverse[i]
            if partial_sum >= x:
                mks[r] = makespan[i]
                seq[r] = sequence[i]
                break

    return seq, mks
