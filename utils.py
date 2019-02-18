import numpy as np

def rng(seed, low, high):
    # Random number generator, as in Taillard's benchmarks paper
    m = 2147483647  # 2^31 - 1
    a = 16807
    b = 127773
    c = 2836
    k = int(seed / b)
    # Update seed
    seed = a * (seed % b) - k * c
    if (seed < 0):
        seed = seed + m
    # Random number between 0 and 1
    val = float(seed) / m
    # Between low and high
    randnum = low + int(val * (high - low + 1))
    return randnum, seed


def random_matrix(mc, jb, seed_value):
    # Generate random mc x jb matrix with rng
    a = np.ndarray((mc, jb))  # Initialize matrix

    # Generate random matrix of times for machines x jobs matrix
    for i in range(mc):
        for j in range(jb):
            a[i, j], seed_value = rng(seed_value, 1, 99)

    return a


def calculate_makespan(a, seq):
    # Order the jobs (rows) in order of the sequence
    a = a[seq]

    b = np.zeros(a.shape)
    jobs = a.shape[0]
    macs = a.shape[1]

    b[0, 0] = a[0, 0]
    # Build first row
    for i in range(1, macs):
        b[0, i] = a[0, i] + b[0, i - 1]
    # Build first column
    for i in range(1, jobs):
        b[i, 0] = a[i, 0] + b[i - 1, 0]
    # Build the rest
    for i in range(1, jobs):
        for j in range(1, macs):
            b[i, j] = a[i, j] + (b[i - 1, j] if b[i - 1, j] > b[i, j - 1] else b[i, j - 1])

    return int(b[-1, -1])


def sort_one_list_by_another(s, m):
    # Sort elements in s and m according to m
    indices = m.argsort()
    s = s[indices]
    m = m[indices]
    return s, m


def sort_and_reduce(s, m):
    s, m = sort_one_list_by_another(s, m)
    s = s[:20]
    m = m[:20]
    return s, m