from collections import defaultdict
testDict = defaultdict(int)

class Book:
    def __init__(self, authName):
        self.authName = authName

testBook = Book("Karam Danial")
testDict[hash(testBook.authName)] = 1
print(testDict)