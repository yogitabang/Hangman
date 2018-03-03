
class HangmanPlayerOne:
	
	def __init__(self,hangmanString):
		self.count = 7
		self.number = len(hangmanString)
		self.hangmanString = hangmanString
		self.playerTwoString = list(self.number)

	def isTheCharacterRight(self,character):
		if(self.count!=0 and isRight(character)):
			tempList = findAll(character)
			for i in range(0,len(tempList):
				playerTwoString.insert(templList(i),character)
		else:
			self.count-=1
		return playerTwoString

	def isRight(self,character):
		if(hangmanString.find(character) != -1):
			return true 
		return false

	def findAll(self,character):
		return [i for i, ltr in enumerate(s) if ltr == ch]

