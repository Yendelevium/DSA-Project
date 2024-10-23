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
- ID (And will be how the BST/AVL Tree will search)
- Reviews?

REVIEW
- Review ID
- Review
- Author

"""

class Game:
    def __init__(self, name, price, rating, game_id):
        self.name = name
        self.price = price
        self.rating = rating
        self.id = game_id
        self.reviews = []  # List of Review objects

class Review:
    def __init__(self, reviewId, reviewText, author):
        self.reviewId = reviewId
        self.reviewText = reviewText#Think of a better name lol
        self.author = author
