import RockPaperScissors
import ScrabbleScore


def main():
	switch()


def switch():

	print("1: Scrabble Score")
	print("2: Rock Paper Scissors")
	print("3: Exit")
	choice = int(input("Enter your choice: "))

	def _ScrabbleScore():
		scrabble = ScrabbleScore.ScrabbleScore()
		scrabble.Play()

	def _RockPaperScissors():
		rps = RockPaperScissors.RockPaperScissors()
		rps.PlayGame()

	def _default():
		print("Incorect option")

	dict = {
		1: _ScrabbleScore,
		2: _RockPaperScissors,
		3: exit,
	}
	dict.get(choice, _default)()


if __name__ == '__main__':
	main()
