# FlowShopProject
## Optimization of permutation flow shop scheduling on the basis of makespan computation using natural algorithms.
Done as a master's degree project at St. Xavier's College, Kolkata, under the supervision of Prof. Siladitya Mukherjee.

Team members: Proyag Pal, Kaustav Basu and Triparna Mukherjee.

A special type of [flow shop scheduling problem](https://en.wikipedia.org/wiki/Flow_shop_scheduling) is the permutation flow shop scheduling problem in which the processing order of the jobs on the resources is the same for each subsequent step of processing.

We used [genetic algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm) to optimize permutation flow shop scheduling problems on the basis of their makespan values.

Evaluated our method by comparing our results against the [benchmarks published by Eric Taillard](http://mistic.heig-vd.ch/taillard/articles.dir/Taillard1993EJOR.pdf).

The Code folder contains:

```genetic.py```: contains the genetic algorithms used - inverse mutation, pairwise swap mutation, ordered crossover.

```Integrated.py```: Runs a GUI to explore the results on our method on the benchmark problems one at a time.

```Run.py```: Runs the optimization algorithm on all the 120 problems in the benchmarks. **WARNING**: Takes hours to run.

```Makespans.xlsx```: Contains the benchmarks and our results along with the average relative percentage difference (ARPD).

```Taillard.xlsx```: Contains Taillard's benchmarks.



### Outline of the algorithm:

1.	Initial sequence of n jobs in ascending order. [0 1 2 ... n]
2.	Start with 4 jobs [0 1 2 3]. Permute 4! = 24 sequences. Set i=4.
3.	Calculate makespan for each of the 24 sequences (using only the corresponding rows of the matrix to calculate). Arrange in ascending order of makespan.
4.	Select best 20 sequences.
5.	Clone using RWS to have 3 * 20 = 60 sequences.
6.	Select best 20 sequences.
7.	For each of 20 sequences, apply Ordered Crossover with the other 19 sequences. => 20 * 19 = 380 sequences.
8.	Select best 20 sequences.
9.	Apply Mutation (tried different types) on each of the 20 sequences to get 20 more sequences => 40 sequences.
10.	Select best 20 sequences.
11.	Increment i. If i>n goto Step 14.
12.	Add i-th job to each of the 20 sequences to each possible position.
13.	Goto step 4.
14.	Select the best sequence.
