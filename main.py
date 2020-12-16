from TournamentResults import *
from Ranking import *
from SimulatedAnnealing import *
import math
from random import randint
import argparse
import time


def main(arg):
    file = open(arg, 'r')

    number_of_participants = int(file.readline())
    participants = [[int(i), participant] for (i, participant) in [file.readline().strip().split(',') for _ in range(number_of_participants)]]

    number_of_matchups = file.readline().split(',')[2]
    print(number_of_matchups)

    results = TournamentResults(participants)
    print(results.get_participant_name(45))

    # Start of the algorithm
    time_start = time.perf_counter()

    # End of the algorithm
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')


if __name__ == "__main__":
    TI = 1.0
    TL = 10
    f = 0.95
    num_non_improve = 5000
    try:
        parser = argparse.ArgumentParser(description='Tournament Directed Graph')
        parser.add_argument('results', type=str, help='Tournament Results')
        args = parser.parse_args()
        main(args.results)
    except:
        main('1994_Formula_One.wmg')
