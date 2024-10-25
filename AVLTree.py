class Node:
    def __init__(self, game):
        self.game = game
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        return node.height if node else 0

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, node):
        if not node or not node.left:
            return node

        node2 = node.left
        temp = node2.right

        node2.right = node
        node.left = temp

        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        node2.height = max(self.getHeight(node2.left), self.getHeight(node2.right)) + 1
        return node2

    def rotateLeft(self, node):
        if not node or not node.right:
            return node

        node2 = node.right
        temp = node2.left

        node2.left = node
        node.right = temp

        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        node2.height = max(self.getHeight(node2.left), self.getHeight(node2.right)) + 1
        return node2

    def insertGame(self, node, game):
        if node is None:
            return Node(game)
        elif game.id < node.game.id:
            node.left = self.insertGame(node.left, game)
        elif game.id > node.game.id:
            node.right = self.insertGame(node.right, game)
        else:  # Equal ids not allowed
            return node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)
        # Left Left Case
        if balance > 1 and game.id < node.left.game.id:
            return self.rotateRight(node)

        # Right Right Case
        if balance < -1 and game.id > node.right.game.id:
            return self.rotateLeft(node)

        # Left Right Case
        if balance > 1 and game.id > node.left.game.id:
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        # Right Left Case
        if balance < -1 and game.id < node.right.game.id:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

    def getMin(self, node):
        if not node:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, node, game):
        if not node:
            return node

        if game.id < node.game.id:
            node.left = self.delete(node.left, game)
        elif game.id > node.game.id:
            node.right = self.delete(node.right, game)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp
            temp = self.getMin(node.right)
            node.game = temp.game
            node.right = self.delete(node.right, temp.game)
        if node is None:
            return node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)
        # Left Left Case
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rotateRight(node)

        # Left Right Case
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        # Right Right Case
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.rotateLeft(node)

        # Right Left Case
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

    def inorderTraversal(self, node):
        if node is None:
            return []
        return self.inorderTraversal(node.left) + [node.game] + self.inorderTraversal(node.right)

    def searchNode(self, node, id):
        if node is None:
            return None
        if node.game.id == id:
            return node.game
        elif id > node.game.id:
            return self.searchNode(node.right, id)
        else:
            return self.searchNode(node.left, id)