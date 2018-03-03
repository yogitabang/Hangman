from HangmanPlayerOne import *
from HangmanPlayerTwo import *
import getpass

print("PLAYER 1")
hangmanString = getpass.getpass("input the string in your mind")
hangmanPlayerOne = HangmanPlayerOne(hangmanString)

print("PLAYER 2")
hangmanPlayerTwo = HangmanPlayerTwo(hangmanPlayerOne.number)
while(hangmanPlayerOne.count != 0):
	character = raw_input("Guess the character")
	tempList = hangmanPlayerOne.isTheCharacterRight(character)
	hangmanPlayerTwo.copyList(tempList)
	if(hangmanPlayerOne.hangmanString.list() == hangmanPlayerTwo.hangmanString)
		print("YOU WIN")
		break
if(hangmanPlayerOne.count == 0)
	print("YOU LOSE :(")
	