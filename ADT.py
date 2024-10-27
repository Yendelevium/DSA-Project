class Game:
    def __init__(self, name, price, genre, rating, game_id):
        self.name = name
        self.price = price
        self.rating = rating
        self.genre = genre  # List of genre's
        self.id = game_id
        self.reviews = []  # List of Review objects

class Review:
    def __init__(self, review, author):
        self.review = review
        self.author = author
