class HangmanPlayer2:
	def __init__(self, number):
		self.number = number
		self.hangmanString = ''

	def isRepeated(self, character):
		if(self.hangmanString.find(character) != -1):
			return True
		return False
			