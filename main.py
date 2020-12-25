from TournamentResults import *
from Ranking import *
from SimulatedAnnealing import *
from ParseResults import *
import math
from random import randint
import argparse
import time


def main(arg):
    results, n = ParseResults.parse(arg)
    initial_ranking = Ranking(results, [i for i in range(1, n + 1)])
    print('Average runtime ≈ 40.0(s) due to shamefully poor programming, please bear with ...')
    # Start of the algorithm
    time_start = time.perf_counter()

    anneal_sim_model = SimulatedAnnealing()
    ranking = anneal_sim_model.annealing_sim(initial_ranking, ti, tl, f, num_non_improve)

    # End of the algorithm
    time_finish = time.perf_counter()
    print(f'Best ranking: {ranking.ranking}')
    print(f'Kemeny Score: {ranking.get_kemeny_score()}')
    print(f'Uphill moves: {anneal_sim_model.get_uphill_moves()}')
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')


if __name__ == "__main__":
    # Initial Temperature
    ti = 1.0
    # Temperature Length
    tl = 10
    # Cooling Ratio
    f = .75
    # Stopping Criterion
    num_non_improve = 5000

    parser = argparse.ArgumentParser(description='Tournament Directed Graph')
    parser.add_argument('results', type=str, help='Tournament Results')
    args = parser.parse_args()
    main(args.results)
