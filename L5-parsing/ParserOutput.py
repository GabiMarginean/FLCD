from Grammar import Grammar
from Parser import Parser

class ParserOutput():

	def __init__(self, grammar_file, output_file = None):
		self.grammar = Grammar(grammar_file)
		self.parser  = Parser(self.grammar)

		self.output_file = output_file


	def check_sequence(self, seq):
		print("Parsing", seq + "...")
		prod = self.parser.parse(seq)

		if prod:
			print("Prod string:", prod)

			if self.output_file:
				with open(self.output_file, 'w') as f:
					f.write(prod)
		
		print("")



if __name__ == '__main__':
	int_parser = ParserOutput("inputs/int_grammar.txt")
	int_parser.check_sequence("-123")
	int_parser.check_sequence("-01")

	sem_parser = ParserOutput("inputs/g1.txt", "out/out1.txt")
	sem_parser.check_sequence("a+a*a")
	sem_parser.check_sequence("a+a-a")