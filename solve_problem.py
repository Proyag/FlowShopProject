import sys
import numpy as np
from itertools import permutations

from utils import *
import genetic


def read_problem(sheet, prob_num):
    jobs = sheet.cell(row=prob_num+3, column=1).value
    machines = sheet.cell(row=prob_num+3, column=2).value
    timeseed = sheet.cell(row=prob_num+3, column=3).value
    prev_makespan = sheet.cell(row=prob_num+3, column=6).value

    return jobs, machines, timeseed, prev_makespan


def write_new_best(prob_num, sequence, makespan, sheet, workbook, benchmark_file='Makespans.xlsx'):
    print("Writing new best for Problem #{:d}".format(prob_num))
    sheet.cell(row=prob_num + 3, column=6).value = makespan
    sheet.cell(row=prob_num + 3, column=7).value = sequence
    workbook.save(benchmark_file)


def solve_benchmark_problem(problem, jobs, machines, timeseed, show_matrix=True):
    # Generate matrix of times
    a = random_matrix(machines, jobs, timeseed)
    print("\nProblem No.:", problem)
    if show_matrix:
        print("Matrix:\n", a)
    # Transpose matrix to calulate makespan
    at = a.transpose()

    # Start with all possible permutations of first 4 jobs
    init_jobs = 4
    init_job_list = list(range(init_jobs))
    # Generate all 24 permutations
    sequence_list = np.array(list(permutations(init_job_list)))

    while init_jobs <= jobs:
        makespan_list = np.array([])
        for seq in sequence_list:
            seq = list(seq)
            makespan_list = np.append(makespan_list, calculate_makespan(at[init_job_list], seq))

        # Sort both arrays in ascending order of makespan
        # and reduce to 20 best sequences
        sequence_list, makespan_list = sort_and_reduce(sequence_list, makespan_list)

        # Roulette wheel .. 3 x 20 output
        sequence_list, makespan_list = genetic.roulette_wheel(sequence_list, makespan_list)

        # Again, sort and reduce to 20
        sequence_list, makespan_list = sort_and_reduce(sequence_list, makespan_list)

        # Now ordered crossover each of the 20 sequences with each other
        # and add to lists
        for i in range(20):
            for j in range(20):
                if i != j:
                    child = genetic.ordered_crossover(sequence_list[i], sequence_list[j])
                    child = np.array(child)
                    sequence_list = np.vstack((sequence_list, child))
                    makespan_list = np.append(makespan_list, calculate_makespan(at[init_job_list], list(child)))

        # Sort both arrays in ascending order of makespan
        # and reduce to 20 best sequences
        sequence_list, makespan_list = sort_and_reduce(sequence_list, makespan_list)

        # Applying mutation. Inverse Mutation.
        for i in sequence_list:
            mutated = genetic.inverse_mutation(i)
            mutated = np.array(mutated)
            sequence_list = np.vstack((sequence_list, mutated))
            makespan_list = np.append(makespan_list, calculate_makespan(at[init_job_list], list(mutated)))

        # Sort both arrays in ascending order of makespan
        # and reduce to 20 best sequences
        sequence_list, makespan_list = sort_and_reduce(sequence_list, makespan_list)

        # Applying another mutation. Pairwise Swap Mutation.
        for i in sequence_list:
            mutated = genetic.pairwise_swap_mutation(i)
            mutated = np.array(mutated)
            sequence_list = np.vstack((sequence_list, mutated))
            makespan_list = np.append(makespan_list, calculate_makespan(at[init_job_list], list(mutated)))

        # Sort both arrays in ascending order of makespan
        # and reduce to 20 best sequences
        sequence_list, makespan_list = sort_and_reduce(sequence_list, makespan_list)

        # Ordered Crossover again
        for i in range(20):
            for j in range(20):
                if i != j:
                    child = genetic.ordered_crossover(sequence_list[i], sequence_list[j])
                    child = np.array(child)
                    sequence_list = np.vstack((sequence_list, child))
                    makespan_list = np.append(makespan_list, calculate_makespan(at[init_job_list], list(child)))

        # Sort both arrays in ascending order of makespan
        # and reduce to 20 best sequences
        sequence_list, makespan_list = sort_and_reduce(sequence_list, makespan_list)

        # Set first element of sorted list as best makespan.
        best_sequence = sequence_list[0]
        best_makespan = makespan_list[0]

        # Bring in next job into every position in sequence_list
        init_jobs += 1
        init_job_list = list(range(init_jobs))
        new_sequence_list = np.array([], dtype=int).reshape(0, init_jobs)
        for s in sequence_list:
            for pos in range(s.size + 1):
                new_sequence_list = np.vstack((new_sequence_list, np.insert(s, pos, init_jobs - 1)))
        sequence_list = new_sequence_list

    return best_sequence, best_makespan
