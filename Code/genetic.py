def inverse_mutation(sequence):
	#Inverts slice between start and end
	from random import randint
	jobs = len(sequence)
	#Generating start and end indices randomly
	start = randint(0, jobs - 2)
	end = randint(start + 1, jobs - 1)

	import numpy as np
	sequence[start:end] = np.fliplr([sequence[start:end]])[0]
	return sequence


def pairwise_swap_mutation(sequence):
	#Swaps start and end positions
	from random import randint
	jobs = len(sequence)
	#Generating start and end indices randomly
	start = randint(0, jobs - 2)
	end = randint(start + 1, jobs - 1)
	
	sequence[start], sequence[end] = sequence[end], sequence[start]
	return sequence


def ordered_crossover(parent1, parent2):
	from random import randint
	jobs = len(parent1)
	#Generating start and end indices randomly
	start = randint(0, jobs - 2)
	end = randint(start + 1, jobs - 1)

	#Initialize child list
	child = [-1] * jobs
	
	#Copy the alleles between start-end from parent1
	child[start:end + 1] = parent1[start:end + 1]

	#Start from 2nd crossover point and copy the rest of the elements in order, cyclically
	parent_index = (end + 1) % jobs
	child_index = (end + 1) % jobs
	while child_index != start:
		if parent2[parent_index] not in child:
			child[child_index] = parent2[parent_index]
			child_index = (child_index + 1) % jobs
		parent_index = (parent_index + 1) % jobs
	return child