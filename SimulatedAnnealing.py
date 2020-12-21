from Ranking import *
import random
import math
import copy


class SimulatedAnnealing(Ranking):
    def __init__(self):
        self.uphill_moves = 0

    # Simulated Annealing Algorithm

    def annealing_sim(self, ranking, ti, tl, f, nun_non_improve):
        current = ranking
        best = ranking
        t = ti
        i = 0

        # Stopping Criterion
        while i < nun_non_improve:
            for _ in range(0, tl):
                # Generating Neighbouring Solution
                potential_ranking = current.get_random_n()
                cost = potential_ranking.get_kemeny_score() - current.get_kemeny_score()

                if cost <= 0:
                    current = potential_ranking
                    if current.get_kemeny_score() < best.get_kemeny_score():
                        best = current
                    else:
                        i += 1
                else:
                    neighbourhood_P = math.e**((-cost)/t)
                    if neighbourhood_P > random.uniform(0.0, 1.0):
                        current = potential_ranking
                        self.uphill_moves += 1
                    i += 1
            t = t * f

        return best

    def get_uphill_moves(self):
        return self.uphill_moves
