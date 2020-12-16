class TournamentResults:
    def __init__(self, participants):
        self.participants = participants
        self.matchups = dict()

    def add_matchup(self, a, b, score):
        matchup = Matchup(a, b)
        self.matchups[matchup] = score

    def get_participant_name(self, participant):
        return self.participants[participant]


class Matchup:
    def __init__(self, a, b):
        self.participant_a = a
        self.participant_b = b

    def reverse(self):
        return Matchup(self.participant_b, self.participant_a)
