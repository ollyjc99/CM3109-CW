class TournamentResults:
    def __init__(self, participants):
        self.participants = participants
        self.matchups = dict()

    def __str__(self):
        return 'Tournament Results Super Class'

    def add_matchup(self, a, b, score):
        matchup = Matchup(a, b)
        self.matchups.update({matchup:score})

    def get_matchup(self, a, b):
        matchup = Matchup(a, b)
        result = self.matchups.get(matchup)
        if result:
            return result
        result = self.matchups.get(matchup.reverse())
        if result:
            return -result

        return None

    def get_participant_name(self, participant):
        return self.participants[participant + -1]


class Matchup:
    def __init__(self, a, b):
        self.participant_a = a
        self.participant_b = b

    def reverse(self):
        return Matchup(self.participant_b, self.participant_a)

    # def __eq__(self, o):
    #     if o.__class__() != self.__class__:
    #         pass

    def __hash__(self):
        return self.participant_a * 65536 + self.participant_b

