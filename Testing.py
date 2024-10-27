from ADT import Game, Review
from AVLTree import AVLTree
from seeds import getGames
import MinHeap
class GameStore:
    def __init__(self):
        self.gameAVL=AVLTree()
        self.gameGraph=None
        self.gameHeap=None
        self.gameTrie=None

    # AVL Tree Stuff
    def getAllGames(self):
        return self.gameAVL.inorderTraversal(self.gameAVL.root)

    def findGame(self,id):
        return self.gameAVL.searchNode(self.gameAVL.root,id)

    def insertGame(self,game):
        self.gameAVL.root=self.gameAVL.insertGame(self.gameAVL.root,game)
        return

    def gameNameSearch(self,gameName):
        # Must return a list of games which match
        # You can have a hashmap which maps the game names to the id, and u can search the id's in an AVL Tree
        # Then return the list of games
        self.findGame("ID GOTTEN FRM HASHMAP")
        return

    def sortRating(self,order):
        if order == "ascending":
            MinH = MinHeap.MinHeap(priority_field="rating")
            
            MinH.importGames()
            sorted_games = MinH.extractSortedGames()
            top_10_games = [
                sorted_games[0],
                sorted_games[1],
                sorted_games[2],
                sorted_games[3], 
                sorted_games[4],
                sorted_games[5],
                sorted_games[6],
                sorted_games[7],
                sorted_games[8],
                sorted_games[9]
            ]
            return top_10_games
        return

    def sortPrice(self,order):
        if order == "ascending":
            MinH = MinHeap.MinHeap(priority_field="price")
            
            MinH.importGames()
            sorted_games = MinH.extractSortedGames()
            top_10_games = [
                sorted_games[0],
                sorted_games[1],
                sorted_games[2],
                sorted_games[3], 
                sorted_games[4],
                sorted_games[5],
                sorted_games[6],
                sorted_games[7],
                sorted_games[8],
                sorted_games[9]
            ]
            return top_10_games
        return

    def getGenreGames(self,genre):
        # Graph
        return
    def gameSelection(self,games):
        print("Enter ID to know more about the following games")
        print("____________________________________")
        for i in games:
            print(i.id,i.name)
            print("Price: ",i.price)
            print("Rating: ",i.rating)
            print("Genre(s)")
            for j in range(0,len(i.genre)):
                print(i.genre[j], end=" ")
            print()
            print("____________________________________")
        gameChoice = int(input())
        retrievedGame = self.findGame(gameChoice)
        if retrievedGame is None:
            raise IndexError("Game doesn't exist")
        print('Name:', retrievedGame.name)
        print('Price:', retrievedGame.price)
        print('Rating:', retrievedGame.rating)
        print('Genre(s):')
        for i in retrievedGame.genre:
            print('\t',i)
        ch=input("Would you like to see the reviews?(Y/N)").upper()

        # Todo : Adding reviews to the game
        if ch=="Y":
            for i in retrievedGame.reviews:
                print("Author:", i.author)
                print("Review:", i.review)
                print()
            ch=input("Press any key to go back to homepage")
            return
        else:
            return
gameStore=GameStore()
games = getGames()
for i in games:
    gameStore.insertGame(i)
id=31 #We alr have 31 games in the tree
while True:
    print("Welcome to <Name>")
    print("Enter the corresponding option number")
    print("1. View All Games") #AVL
        # Then we can do the selection process again
    print("2. Search for a game") #Trie
        #Searching - Exact Match Search, Search by Substring,
        #Auto-Correct - (Use a Trie-based Levenshtein Distance to find titles within a 1-2 character difference) - Trie

        #AFTER SELECTING THE GAME
        #Add review - AVL
        #Show related games - Graph
        #Show related Genres - Graph
    print("3. Show top 10 Games by Price") #Heap
        #Then we can do the selection process again
    print("4. Show top 10 Games by Rating") #Heap
        # Then we can do the selection process again
    print("5. Show Games by Genre") #Graph
        # Then we can do the selection process again
    print("6. Add a Game") #AVL, Graph, Trie, Heap - Insert in all
    print("Press Enter key to exit")

    choice=input()
    if choice=='':
        print("Thank you for stopping by!")
        break
    choice=int(choice)
    if choice==1:
        allGames=gameStore.getAllGames()
        gameStore.gameSelection(allGames)

    elif choice==2:
        print("Enter the name of the game")
        gameSearch=input()
        foundGames=gameStore.gameNameSearch(gameSearch)
        gameStore.gameSelection(foundGames)

    elif choice==3:
        print("1. High to Low")
        print("2. Low to High")
        ch=int(input())
        if ch==1:
            sortedGames=gameStore.sortPrice("descending")
            gameStore.gameSelection(sortedGames)

        elif ch==2:
            sortedGames = gameStore.sortPrice("ascending")
            gameStore.gameSelection(sortedGames)
        else:
            raise IndexError("Choose correct value")
            pass

    elif choice==4:
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
            pass

    elif choice==5:
        print("Select Genre")
        print("1. Idk")
        print("2. Idk")
        print("3. Idk")

        genre=input().upper()
        genreGames=gameStore.getGenreGames(genre)
        gameStore.gameSelection(genreGames)

    elif choice==6:
        name=input("Game Name\t:")
        price=input("Price\t:")
        rating=input("Rating\t:")
        genre=input("Genre(separated by space)\t:").split()
        newGame= Game(name,price,genre,rating,id)
        gameStore.insertGame(newGame)
        print("Successfully added a new game!")
        id+=1
    else:
        print("Not an option, Thank you for stopping by!")
        break
