# FlowShopProject
## Optimization of permutation flow shop scheduling on the basis of makespan computation using natural algorithms.
Done as a master's degree project at St. Xavier's College, Kolkata, under the supervision of Prof. Siladitya Mukherjee.

Team members: Proyag Pal, Kaustav Basu and Triparna Mukherjee.

<https://en.wikipedia.org/wiki/Flow_shop_scheduling>

A special type of flow shop scheduling problem is the permutation flow shop scheduling problem in which the processing order of the jobs on the resources is the same for each subsequent step of processing.

<https://en.wikipedia.org/wiki/Genetic_algorithm>

We used genetic algorithms to optimize permutation flow shop scheduling problems on the basis of their makespan values.

<http://mistic.heig-vd.ch/taillard/articles.dir/Taillard1993EJOR.pdf>

Evaluated our method by comparing our results against the benchmarks published by Eric Taillard.

The Code folder contains:

```genetic.py```: contains the genetic algorithms used - inverse mutation, pairwise swap mutation, ordered crossover.

```Integrated.py```: Runs a GUI to explore the results on our method on the benchmark problems one at a time.

```Run.py```: Runs the optimization algorithm on all the 120 problems in the benchmarks. **WARNING**: Takes hours to run.

```Makespans.xlsx```: Contains the benchmarks and our results along with the average relative percentage difference (ARPD).

```Taillard.xlsx```: Contains Taillard's benchmarks.
