class State:
	def __init__(self, name):
		self.name = name
		self.transitions = []

	def add_transition(self, transition):
		self.transitions.append(transition)

	def __str__(self):
		node = "(%s):\n" % self.name
		for transition in self.transitions:
			node += "\t" + transition + "\n"
		return node

	def __add__(self, other):
		return str(self) + other

	def __radd__(self, other):
		return other + str(self)

	def equals(self, node):
		ok = (self.name == node.name)
		if len(self.transitions) == len(node.transitions):
			for i in range(len(self.transitions)):
				ok = ok and (self.transitions[i] == node.links[i])
			return ok
		else:
			return False

class Transition:
	def __init__(self, from_state, value, to_state):
		self.from_state = from_state
		self.value = value
		self.to_state = to_state

	def accepts(self, value):
		return self.value == value

	def __str__(self):
		return "(%s --[%s]--> %s)" % (self.from_state.val, self.value, self.to_state.val)

	def __add__(self, other):
		return str(self) + other

	def __radd__(self, other):
		return other + str(self)

	def equals(self, link):
		return (self.from_state == link.from_state) and (self.value == link.value) and (self.to_state == link.to_state)


class RangeTransition(Transition):
	def __init__(self, from_state, value, to_state):
		super(RangeTransition, self).__init__(from_state, value, to_state)
		self.range = [s.strip() for s in value.split("-")]

	def accepts(self, value):
		return self.range[0] <= value <= self.range[1]


class Automata:

	def __init__(self, filename):
		self._read_file(filename)


	def _read_file(self, filename):
		with open(filename) as f:
			lines = [s.strip() for s in f.read().splitlines()]

			self.states = [State(val) for val in lines[0].split(' ')]

			self.initial_state = self._get_state(lines[1].split(' ')[0])

			self.final_states = [self._get_state(val) for val in lines[2].split(' ')]
			self.alphabet = lines[3].strip()


			for i in range(4, len(lines)):
				tkn = [l.strip() for l in lines[i].split("->")]
				tkn[1] = tkn[1].split(" ")
				
				fr = self._get_state(tkn[0])
				to = self._get_state(tkn[1][0])

				if "-" in tkn[1][1] and len(tkn[1][1]) > 1:
					fr.add_transition(RangeTransition(fr, tkn[1][1], to))
				else:
					fr.add_transition(Transition(fr, tkn[1][1], to))

	def accepts(self, string):
		state = self.initial_state
		for character in string:

			if not state:
				return False

			state = self._get_next_node(state, character)

		return state in self.final_states

	def _get_state(self, name):
		for state in self.states:
			if state.name == name:
				return state
		return None
		
	def _get_next_node(self, current_node, value):
		for transition in current_node.transitions:
			if transition.accepts(value):
				return transition.to_state
		return None

	def __str__(self):
		automata = "Initial state: %s\nTerminal state: %sAlphabet: %s\n" % (self.initial_state.val, *self.final_states, self.alphabet)
		for state in self.states:
			automata += state
		return automata

	def states(self):
		print("".join(map(str, self.states)))

	def alphabet(self):
		print(self.alphabet)

	def transitions(self):
		print("".join(map(str, self.states)))

	def final_states(self):
		print("".join(map(str, self.final_states)))


	def __add__(self, other):
		return str(self) + other

	def __radd__(self, other):
		return other + str(self)
