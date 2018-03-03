from HangmanPlayer import *
import getpass

print("PLAYER 1")
hangmanString = getpass.getpass("input the string in your mind")
hangmanPlayer = HangmanPlayer(hangmanString)

print("PLAYER 2")
while(hangmanPlayer.count != 0):
	character = raw_input("Guess the character")
	tempList = hangmanPlayer.isTheCharacterRight(character)
	if(hangmanPlayer.win == hangmanPlayer.number):
		print("YOU WIN")
		break
if(hangmanPlayer.count == 0):
	print("YOU LOSE :(")
	