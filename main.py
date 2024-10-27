"""
Game Stop
1. Find games - Use Trie to get related names- Then choose which game u want, and it will be searched by BST/AVL Tree
I'm thinking each game will have an ID and it will be how the BST/AVL Tree will be made
Ask the user to enter the ID of the game

2. Sort games based on price, rating - Heaps- 2 diff heaps, one for sorting via rating, other via price
Can have additional functionality to sort from low to high or high to low

3. Add games - Insert in BST/AVL Tree

4. Similar Games - Graphs - Based on Genre. Each Genre can have it's graph?? And use closest neighbours to give some
suggestions about similar games. This can also be used for some sort of filtering via genre or smtg

ADT:
GAME
- Game Name
- Price
- Rating
- Genre(s)
- ID (And will be how the BST/AVL Tree will search)
- Reviews?

REVIEW
- Review
- Author

"""
from ADT import Game, Review
from Trie import Trie
from AVLTree import AVLTree
from seeds import getGames
from Minheap import MinHeap
from MaxHeap import MaxHeap 
from Graph import GameGraph

class GameStore:
    def __init__(self):
        self.gameAVL = AVLTree()
        self.gameHeapRating = MinHeap("rating")
        self.gameHeapPrice = MinHeap("price")
        self.gameHeapRatingDesc = MaxHeap("rating")
        self.gameHeapPriceDesc = MaxHeap("price")
        self.gameGraph = GameGraph()
        self.gameTrie = Trie()
        self.gameNameToId = {}

    # AVL Tree Stuff
    def getAllGames(self):
        return self.gameAVL.inorderTraversal(self.gameAVL.root)

    def findGame(self, id):
        return self.gameAVL.searchNode(self.gameAVL.root, id)

    def insertGame(self, game):
        self.gameAVL.root = self.gameAVL.insertGame(self.gameAVL.root, game)
        self.gameTrie.insert(game.name)
        self.gameNameToId[game.name] = game.id
        self.gameHeapPrice.insert(game)
        self.gameHeapPriceDesc.insert(game)  # Add to descending price heap
        self.gameHeapRating.insert(game)
        self.gameHeapRatingDesc.insert(game)  # Add to descending rating heap
        self.gameGraph.add_game(game, game.genre)
        for gen in game.genre:
            l = len(self.gameGraph.genre_map)
            if gen not in self.gameGraph.genre_map.values():
                self.gameGraph.genre_map[str(l + 1)] = gen
        return

    def gameNameSearch(self, gameName):
        matchedNames = self.gameTrie.search(gameName)
        if isinstance(matchedNames, bool) or not matchedNames:
            matchedNames = self.gameTrie.autocomplete(gameName)
            if not matchedNames:
                matchedNames = self.gameTrie.autocorrect(gameName)
        matchedGames = [self.findGame(self.gameNameToId[name]).id for name in matchedNames]
        if len(matchedNames) > 1:
            self.gameSelection([self.findGame(self.gameNameToId[name]) for name in matchedNames])
        elif len(matchedNames) == 1:
            self.game_info(matchedGames[0])
        else:
            print("No games found with the entered name")

    def sortRating(self, order):
        if order == "ascending":
            return self.gameHeapRating.extractSortedGames()
        elif order == "descending":
            return self.gameHeapRatingDesc.extractSortedGames()
        return []

    def sortPrice(self, order):
        if order == "ascending":
            return self.gameHeapPrice.extractSortedGames()
        elif order == "descending":
            return self.gameHeapPriceDesc.extractSortedGames()
        return []

    def getGenreGames(self, genre):
        return self.gameGraph.getGenreGames(genre)

    def gameSelection(self, games):
        print("Enter ID to know more about the following games")
        print("____________________________________")
        for i in games:
            print(i.id, i.name)
            print("Price: ", i.price)
            print("Rating: ", i.rating)
            print("Genre(s):", " ".join(i.genre))
        print("____________________________________")
        search_id = int(input())
        if search_id in self.gameNameToId.values():
            self.game_info(search_id)
        else:
            print("Invalid Game ID")

    def game_info(self, gameChoice):
        retrievedGame = self.findGame(gameChoice)
        if retrievedGame is None:
            raise IndexError("Game doesn't exist")
        print('Name:', retrievedGame.name)
        print('Price:', retrievedGame.price)
        print('Rating:', retrievedGame.rating)
        print('Genre(s):')
        for i in retrievedGame.genre:
            print('\t', i)

        similar_games = self.gameGraph.similarGames(retrievedGame)
        if similar_games: 
            print("\nSimilar Games: ")
            for game_name in similar_games:
                print("\t", game_name)
        else:
            print("\nNo Similar Games")
        
        ch = input("Would you like to see the reviews?(Y/N)").upper()
        if ch=="Y":
            for k,v in retrievedGame.reviews.items():
                print("Author:", k)
                print("Review:", v)
                print()
            ch=input("Press any key to go back to homepage")
            return
        else:
            return

# Driver Code
gameStore = GameStore()
games = getGames()
for i in games:
    gameStore.insertGame(i)
id = 37  # We already have 37 games in the tree

while True:
    print("Welcome to <Name>")
    print("Enter the corresponding option number")
    print("1. View All Games")
    print("2. Search for a game")
    print("3. Show top 10 Games by Price")
    print("4. Show top 10 Games by Rating")
    print("5. Show Games by Genre")
    print("6. Add a Game")
    print("Press Enter key to exit")

    choice = input()
    if choice == '':
        print("Thank you for stopping by!")
        break
    choice = int(choice)
    
    if choice == 1:
        allGames = gameStore.getAllGames()
        gameStore.gameSelection(allGames)

    elif choice == 2:
        print("Enter the name of the game")
        gameSearch = input()
        gameStore.gameNameSearch(gameSearch)

    elif choice == 3:
        print("1. High to Low")
        print("2. Low to High")
        ch = int(input())
        if ch == 1:
            sortedGames = gameStore.sortPrice("descending")
            gameStore.gameSelection(sortedGames)
        elif ch == 2:
            sortedGames = gameStore.sortPrice("ascending")
            gameStore.gameSelection(sortedGames)
        else:
            raise IndexError("Choose correct value")

    elif choice == 4:
        print("1. High to Low")
        print("2. Low to High")
        ch = int(input())
        if ch == 1:
            sortedGames = gameStore.sortRating("descending")
            gameStore.gameSelection(sortedGames)
        elif ch == 2:
            sortedGames = gameStore.sortRating("ascending")
            gameStore.gameSelection(sortedGames)
        else:
            raise IndexError("Choose correct value")

    elif choice == 5:
        print("Enter the number next to genre")
        for k, v in gameStore.gameGraph.genre_map.items():
            print(k, ":", v)

        genre_choice = input()
        genre = gameStore.gameGraph.genre_map.get(genre_choice)

        if genre:
            genreGames = gameStore.getGenreGames(genre)
            gameStore.gameSelection(genreGames)
        else:
            print("Invalid genre choice. Please select a valid option.")

    elif choice == 6:
        name = input("Game Name\t:")
        price = float(input("Price\t:"))
        rating = float(input("Rating\t:"))
        genre = input("Genre (separated by space)\t:").split()
        genre = [g.capitalize() for g in genre]  # Capitalize each genre
        id += 1
        newGame = Game(name, price, genre, rating, id)
        gameStore.insertGame(newGame)
        print("Successfully added a new game!")
    else:
        print("Not an option, Thank you for stopping by!")
        break

