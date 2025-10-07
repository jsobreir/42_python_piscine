import sys

def main():
	try:
		text = sys.argv
		print(text)
		assert len(text) <= 2, "Assertion Error: invalid input"
		if len(text) < 2:
				text.append(input("What is the text to count?\n") + "\n")
		punctuation_marks = ".!?,:;-()'"
		text = text[1]
		print("The text contains", sum(1 for c in text), "characters:")
		print(sum(1 for c in text if c.isupper()), "upper letters")
		print(sum(1 for c in text if c.islower()), "lower letters")
		print(sum(1 for c in text if c in punctuation_marks), "punctuation marks")
		print(sum(1 for c in text if c in " \t\n\r"), "spaces")
		print(sum(1 for c in text if c.isdigit()), "digits")
	except AssertionError as error:
		print(error)

if __name__ == "__main__":
	main()