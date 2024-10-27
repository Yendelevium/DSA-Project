from collections import defaultdict

# Used Adjacency List representation of Graph
class GameGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.genre_map = {
            "1": "Action",
            "2": "Adventure",
            "3": "RPG",
            "4": "Indie",
            "5": "Multiplayer",
            "6": "Sports",
            "7": "Free To Play",
        }

    # O(g+n) where g is number of genres and n is number of games associated with the genre.
    def add_game(self, game, genres):
        for genre in genres:
            if genre not in self.graph:
                self.graph[genre] = []
            self.graph[genre].append(game)

            for other_game in self.graph[genre]:
                if other_game != game:
                    self.graph[game].append(other_game)
                    self.graph[other_game].append(game)

    # O(g*n) where g is number of genres and n is the number of games associated with the genre.
    def similarGames(self, game):
        simgames = set()
        if game not in self.graph:
            return

        for genre in self.graph[game]:
            for sim in self.graph[genre]:
                if sim != game:
                    simgames.add(sim.name)
        return list(simgames)

    #O(1) Constant Time Complexity as we directly return the vertices that genre is connected with.
    def getGenreGames(self, genre):
        if genre not in self.graph:
            return "Genre does not exist."
        return self.graph[genre]


