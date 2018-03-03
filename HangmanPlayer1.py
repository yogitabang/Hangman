
class HangmanPlayer1:
	
	def __init__(self,hangmanString):
		self.count = 7
		self.number = len(hangmanString)
		self.hangmanString = hangmanString
		self.playerTwoString = ['0'] * self.number 
		self.win = 0

	def isTheCharacterRight(self,character):
		if(self.count!=0 and self.isRight(character)):
			tempList = self.findAll(self.hangmanString,character)
			print(self.findAll(self.hangmanString,character))
			for i in range(0,len(tempList)):
				self.playerTwoString.insert(int(tempList[i]),character)
			self.win += len(tempList)
		else:
			self.count-=1
		return self.playerTwoString

	def isRight(self,character):
		if(self.hangmanString.find(character) != -1):
			return True 
		return False

	def findAll(self,s,character):
		return [i for i, ltr in enumerate(s) if ltr == character]

