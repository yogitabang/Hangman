from HangmanPlayer1 import *
from HangmanPlayer2 import *
import getpass

print("PLAYER 1")
hangmanString = getpass.getpass("input the string in your mind")
hangmanPlayer1 = HangmanPlayer1(hangmanString)

print("PLAYER 2")
hangmanPlayer2 = HangmanPlayer2(hangmanPlayer1.number)
while(hangmanPlayer1.count != 0):
	character = raw_input("Guess the character")
	tempList = hangmanPlayer1.isTheCharacterRight(character)
	hangmanPlayer2.copyList(tempList)
	tempString = ''.join(hangmanPlayer2.hangmanString)
	if(hangmanPlayer1.win == hangmanPlayer1.number):
		print("YOU WIN")
		break
if(hangmanPlayer1.count == 0):
	print("YOU LOSE :(")
	