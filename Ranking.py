from TournamentResults import *
import random
import time


class Ranking(TournamentResults):
    def __init__(self, results, ranking, ks=None):
        self.ranking = ranking
        self.results = results
        if ks:
            self.ks = ks
        else:
            self.ks = self.calculate_ks()

    # Calculates the Kemeny score of a ranking

    def calculate_ks(self):
        pos = self.ranking.copy()
        ks = 0

        for participant_a in range(1, len(self.ranking) + 1):
            for participant_b in range(participant_a + 1, len(self.ranking) + 1):
                result = self.results.get_matchup(participant_a, participant_b)
                if not result:
                    continue

                if pos.index(participant_a) > pos.index(participant_b) and result > 0 or pos.index(participant_a) < pos.index(participant_b) and result < 0:
                    ks += abs(result)
        self.ks = ks
        return ks

    # Return Kemeny Score

    def get_kemeny_score(self):
        return self.calculate_ks()

    # Moves a random participant to a random position

    def get_random_n(self):
        old_rank = int(random.uniform(0, 1.0) * len(self.ranking))
        new_rank = old_rank
        difference = 0

        while difference == 0 or (difference == 1 and random.uniform(0.0, 1.0) < 0.5):
            new_rank = int(random.uniform(0.0, 1.0) * len(self.ranking))
            difference = abs(new_rank - old_rank)

        ranking = self.ranking.copy()
        ranking[new_rank - 1] = self.ranking[int(old_rank) - 1]
        source, target = 0, 0
        while target < len(ranking) and source < len(ranking):
            if source == old_rank:
                source += 1
            if target == new_rank:
                target += 1

            ranking[target - 1] = self.ranking[source - 1]
            source += 1
            target += 1
        return Ranking(self.results, ranking, self.calculate_n_ks(old_rank, new_rank))

    # An attempt speed up runtime by not completely recalculating the Kenemy Score but isn't used as it doesn't work

    def calculate_n_ks(self, old_rank, new_rank):
        participant = self.ranking[old_rank - 1]

        ks = self.ks

        count = 0
        if new_rank < old_rank:
            count = 1
        else:
            count = -1
        for i in range(new_rank, old_rank, count):
            result = self.results.get_matchup(participant, self.ranking[i - 1])

            if not result:
                continue

            if old_rank > i ^ result > 0:
                ks -= abs(result)
            else:
                ks += abs(result)

        return ks