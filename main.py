from collections import Counter, OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        # Sort the players based on score, games played, and player order
        sorted_players = sorted(self.standings.keys(), key=lambda player: (-self.standings[player]['score'], self.standings[player]['games_played'], list(self.standings.keys()).index(player)))

        # Get the player at the specified rank (adjusting for 0-based index)
        if 1 <= rank <= len(sorted_players):
            return sorted_players[rank - 1]
        else:
            return None

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))  # Should print "Chris"
