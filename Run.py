# Use this program to write to Excel
import numpy as np
import openpyxl as ox
import sys

from solve_problem import read_problem, solve_benchmark_problem, write_new_best

benchmark_file = 'Makespans.xlsx'
taillard_file = ox.load_workbook(benchmark_file)  # Load workbook
taillard = taillard_file.get_sheet_by_name('Sheet1')  # Load sheet


if __name__ == '__main__':
    # To make command line print complete nd arrays.
    np.set_printoptions(threshold=sys.maxsize)
    # Run for entire 120 problem range
    for problem in range(0, 120):
        jobs, machines, timeseed, prev_best_makespan = read_problem(taillard, problem)

        best_sequence, best_makespan = \
            solve_benchmark_problem(problem, jobs, machines, timeseed, show_matrix=False)

        best_sequence = list(map(int, best_sequence))
        best_sequence = list(map(str, best_sequence))
        best_sequence = ', '.join(best_sequence)

        print("Jobs: ", jobs, "\nMachines: ", machines, "\nTimeseed: ", timeseed, "\nOptimal sequence: ", best_sequence, "\nOptimal makespan: ", best_makespan)

        if best_makespan <= prev_best_makespan:
            write_new_best(problem, best_sequence, best_makespan,
                           taillard, taillard_file, benchmark_file=benchmark_file)
            taillard.cell(row=problem + 3, column=6).value = best_makespan
            taillard.cell(row=problem + 3, column=7).value = best_sequence
            taillard_file.save('Makespans.xlsx')
