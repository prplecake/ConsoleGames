import ScrabbleScore


def countLetters(letterDict):
	count = 0
	for v in letterDict.values():
		count += len(v)
	assert count == 26, "Should be 26"


def main():
	scrabble = ScrabbleScore.ScrabbleScore
	countLetters(scrabble.letterScore)


if __name__ == '__main__':
	main()
