EPS = 'ε'

class Grammar():
	
	def __init__(self, fileName):
		
		self.non_terminals	= []
		self.terminals 		= []
		self.start 			= None
		self.productions 	= {}
		self.prod_idx 	    = {}

		self._readFile(fileName)

		for (idx, prod) in enumerate(self.productions.keys(), 1):
			self.prod_idx[prod] = idx


	def _readFile(self, fileName):
		with open(fileName) as f:

			
			self.non_terminals = [t.strip() for t in f.readline().split(',')]
			self.terminals = [t.strip() for t in f.readline().split(',')]
			self.start = f.readline().strip()


			while (line := f.readline().rstrip()):
				rule = line.split("->")
				lhs = rule[0].rstrip()
				val = [t.strip() for t in rule[1].split('|')]
				self.productions[lhs] = val


	def get_terminals(self):
		return self.terminals

	def get_non_terminals(self):
		return self.non_terminals

	def print_non_terminals(self):
		print(self.non_terminals)

	def print_terminals(self):
		print(self.terminals)

	def print_productions(self):
		print(self.productions)

	def get_productions_for_nonterminal(self, nonterm):
		res = []
		for prod in self.productions:
			for rule in self.productions[prod]:
				if nonterm in rule:
					res.append(prod)
		
		return res   

	def cfg_check(self):
		for prod in self.productions:
			if len(prod[0]) == 1:
				if prod[0] not in self.non_terminals:
					return False
			else:
				return False
		return True
