from Grammar import Grammar, EPS
import copy
import pandas as pd

class Parser():

	def __init__(self, grammar):
		self.grammar 	  = grammar
		self.follow_dict  = {}
		self.ll1Table 	  = []

		self.generate_follow_dict()
		self.gen_parsing_table()

	def first(self, s):
		c = s[0]
		ans = set()
		if c in self.grammar.get_non_terminals():
			for st in self.grammar.productions[c]:
				if st == EPS:				
					if len(s) != 1:
						ans = ans.union(first(s[1:], self.grammar.productions))
					else:
						ans = ans.union(EPS)
				else:	
					first = self.first(st)
					ans = ans.union(x for x in first)
		else:
			ans = ans.union(c)

		return ans

	def generate_follow_dict(self):
		for i in self.grammar.productions:
			self.follow_dict[i] = set()
		
		self.follow_dict[self.grammar.start] = {'$'}

		while True:
			before_dict = copy.deepcopy(self.follow_dict)
			for left, values in self.grammar.productions.items():
				for value in values:
					value = value.split()
					length = len(value)
					for i in range(length):
						if value[i][0] in self.grammar.get_non_terminals():
							if i == length-1:
								self.follow_dict[value[i]] = self.follow_dict[value[i]].union(self.follow_dict[left])
							else:
								next_follow = self.first(value[i+1:])
								self.follow_dict[value[i]] = self.follow_dict[value[i]].union(next_follow)
								if EPS in next_follow:
									self.follow_dict[value[i]] -= {EPS}
									self.follow_dict[value[i]] = self.follow_dict[value[i]].union(self.follow_dict[left])
			
			if self.follow_dict == before_dict:
				break

	def gen_parsing_table(self):
	
		self.parsing_table = {}
		for key in self.grammar.productions:
			for value in self.grammar.productions[key]:
				if value != EPS:
					for element in self.first(value):
						self.parsing_table[key, element] = value
				else:
					for element in self.follow_dict[key]:
						self.parsing_table[key, element] = value


	def print_parsing_table(self):
		new_table = {}
		for pair in self.parsing_table:
			new_table[pair[1]] = {}

		for pair in self.parsing_table:
			new_table[pair[1]][pair[0]] = self.parsing_table[pair]

		print (pd.DataFrame(new_table).fillna('x'))


	def parse(self, sequence):

		reject = 0
		sequence = sequence + "$"
		stack = []
		PI = ""
		
		stack.append("$")
		stack.append(self.grammar.start)

		input_len = len(sequence)
		index = 0

		while len(stack) > 0:
			top = stack[len(stack)-1]
			curr = sequence[index]

			if top == curr:
				stack.pop()
				index += 1	
			else:	
				key = top, curr
	
				if key not in self.parsing_table:
					print("Unexpected symbol '{}' at index {}: {}".format(key[1], index, sequence[index-1:index+2]))
					reject = 1		
					break

				value = self.parsing_table[key]
				if value != EPS:
					value = value.split(" ")[::-1]
			
					stack.pop()

					for element in value:
						if element != ' ':
							stack.append(element)

					PI += str(self.grammar.prod_idx[key[0]])
				else:
					stack.pop()		

		if reject == 0:
			print ("Sequence accepted!")
			return PI
		else:
			print ("Sequence rejected!")	
			return None

