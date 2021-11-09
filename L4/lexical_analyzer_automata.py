import sys
sys.path.insert(1, '../L2')
sys.path.insert(1, '../L3')

from symbol_table import SymbolTable
from regex import *
from automata import Automata

TOKEN_FILE = "../L3/input/token.in"
SEP_FILE   = "../L3/input/separators.in"

INT_AUTOMATA_FILE = "inputs/int_FA.in"
ID_AUTOMATA_FILE  = "inputs/identif_FA.in"

OUT_ST  = "../L3/output/ST.out"
OUT_PIF = "../L3/output/PIF.out"

class LexicalAnalyzer():

	def __init__(self, token_file, separators_file): 
		self._st = SymbolTable()
		self._pif = []
		self._tokens = self._readFile(token_file)
		self._separators = self._readFile(separators_file)
		self._identifAutomata = Automata(INT_AUTOMATA_FILE)
		self._intAutomata = Automata(ID_AUTOMATA_FILE)


	def _readFile(self, token_file):
		with open(token_file) as f:
			return [s.strip() for s in f.read().splitlines()]

	def _isConstant(self, word):
		return any([reg.match(word) for reg in CONST_REG_LIST]) or self._intAutomata.accepts(word)

	def _isIdentifier(self, word):
		return self._identifAutomata.accepts(word)

	def _isToken(self, word):
		return word in self._tokens

	def _isComment(self, line):
		return any([reg.match(line) for reg in COMM_REG_LIST])

	def _removeSeparators(self, token):
		token = token.translate({ord(x): '' for x in self._separators})
		return token

	def _writeData(self):
		with open(OUT_ST, 'w') as f:
			f.write(str(self._st))

		with open(OUT_PIF, 'w') as f:
			for item in self._pif:
				f.write("%s\n" % str(item))


	def analyze(self, input_file):
		errors = False

		with open(input_file) as f:
			for i, line in enumerate(f.readlines()):

				if self._isComment(line):
					continue

				for token in line.split(" "):
					token = token.strip()

					if not token:
						continue

					token = self._removeSeparators(token)

					if self._isToken(token):
						self._pif.append((token, 0))
					elif self._isIdentifier(token) or self._isConstant(token):
						index = self._st.pos(token)
						self._pif.append((token, index))
					else:
						errors = True
						print("Syntax Error: line " + str(i + 1) + " at: '" + token + "'")

		if not errors:
			print("Lexically correct")
		
		self._writeData()

		


la = LexicalAnalyzer(TOKEN_FILE, SEP_FILE)
la.analyze("../L1_a/p2.txt")
