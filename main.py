from HangmanPlayer import *
from HangmanPlayer2 import *
import getpass

print("PLAYER 1")
hangmanString = getpass.getpass("input the string in your mind")
hangmanPlayer = HangmanPlayer(hangmanString)

print("PLAYER 2")
hangmanPlayer2 = HangmanPlayer2(hangmanPlayer.number)
while(hangmanPlayer.count != 0):
	
	character = raw_input("Guess the character")
	if(not hangmanPlayer2.isRepeated(character)):
		tempList = hangmanPlayer.isTheCharacterRight(character)
		hangmanPlayer2.hangmanString = ''.join(hangmanPlayer.playerTwoString)
		print(hangmanPlayer2.hangmanString)
		if(hangmanPlayer.win == hangmanPlayer.number):
			print("YOU WIN")
			break

if(hangmanPlayer.count == 0):
	print("YOU LOSE :(")
	