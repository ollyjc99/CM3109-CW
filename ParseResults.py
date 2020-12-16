from TournamentResults import *


class parse_results(TournamentResults):
        @staticmethod
        def parse(filename):
            file = open(filename, 'r')
            number_of_participants = int(file.readline())
            participants = [[int(i), participant] for (i, participant) in [file.readline().strip().split(',') for _ in range(number_of_participants)]]

            results = TournamentResults(participants)
            number_of_matchups = int(file.readline().split(',')[2])

            for _ in range(number_of_matchups):
                matchup = file.readline().strip().split(',')
                participant_a = int(matchup[0])
                participant_b = int(matchup[1])
                score = int(matchup[2])
                results.add_matchup(participant_a, participant_b, score)
            file.close()

            return results
