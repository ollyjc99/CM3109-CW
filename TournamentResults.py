class TournamentResults:
    def __init__(self, participants):
        self.participants = participants
        self.matchups = dict()

    # Adds each matchup with the resulting score to the dictionary matchups

    def add_matchup(self, a, b, score):
        matchup = Matchup(a, b)
        self.matchups.update({matchup: score})

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

    def __eq__(self, Obj):
        if Obj.__class__.__name__ != self.__class__.__name__:
            return False

        return self.participant_a == Obj.participant_a and self.participant_b == Obj.participant_b

    def __hash__(self):
        return self.participant_a * 65536 + self.participant_b

