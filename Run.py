# Use this program to write to Excel
import numpy as np
import openpyxl as ox
import sys

from solve_problem import read_problem, solve_benchmark_problem, write_new_best

benchmark_file = 'Makespans.xlsx'
taillard_file = ox.load_workbook(benchmark_file)  # Load workbook
taillard = taillard_file.get_sheet_by_name('Sheet1')  # Load sheet


def run_main(problem):
    jobs, machines, timeseed, prev_best_makespan = read_problem(taillard, problem)

    best_sequence, best_makespan = \
        solve_benchmark_problem(problem, jobs, machines, timeseed, show_matrix=False)

    best_sequence = list(map(int, best_sequence))
    best_sequence = list(map(str, best_sequence))
    best_sequence = ', '.join(best_sequence)

    print("Jobs: ", jobs, "\nMachines: ", machines, "\nTimeseed: ", timeseed, "\nOptimal sequence: ", best_sequence, "\nOptimal makespan: ", best_makespan)

    if best_makespan < prev_best_makespan:
        write_new_best(problem, best_sequence, best_makespan,
                       taillard, taillard_file, benchmark_file=benchmark_file)

if __name__ == '__main__':
    # To make command line print complete nd arrays.
    np.set_printoptions(threshold=sys.maxsize)

    if len(sys.argv) == 1:
        # Run for entire 120 problem range
        print("No argument given; running all benchmarks in sequence")
        for problem in range(0, 120):
            run_main(problem)
    else:
        try:
            problem = int(sys.argv[1])
        except ValueError:
            print("Invalid argument - only argument should be a problem number (0-119)")
            exit(1)
        if not 0 <= problem < 120:
            print("There are only 120 problems (numbered 0-119)")
            exit(1)
        run_main(problem)
