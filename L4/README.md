# Finite Automata



## Interface

- `Automata(inputFile : str)`

  where `inputFile` is a text file representing the finite automata in the following format:

  ```c
  line_1        = states_lst   			/* list of all states 					*/
  line_2        = state.                          /* initial state                                        */
  line_3        = states_lst			/* final states 					*/
  line_4        = str				/* alphabet 						*/
  rest_lines    = state "->" state str		/* transitions (from -> to value)			*/
  
  states_lst 	= state | states_lst
  state           = letter | (letter){letter}{digit}{lne}
  letter          =  "a" | "b" | ... | "A" | "B" | ... | "Z"
  digit		= "0" | "1" |...| "9"
  lne 		= "_" | "-"
  str 		= {letter | digit | lne}
  ```

  > If a transition has multiple values/ranges ie. `a-z`, `A-Z`, `-`, a transition must be specified for each of them. For example the following two are equivalent:
  >
  > ```c
  > s0 -> s1 a-z
  > s0 -> s1 A-Z
  > s0 -> s1 _
  > ```
  >
  > ![multiple-value-transition](img/example.svg?raw=true "Multiple valued transition")

- `accepts(sequence : str)`

  verifies wether the automata accepts thee sequence or not

- `states()`

  prints the states of the automata

- `alphabet()`

  prints the alphabet of the automata

- `transitions()`

  prints the transitions of the automata

- `final_states()`

  prints the final states of the automata



## Implementation

The `Automata` class uses the following classes internally:

- `State` class which represents a state having a name and a list of `Transition` objects

  ```python
  class State:
  	def __init__(self, name):
  		self.name = name
  		self.transitions = []
  ```

- `Transition`representing a transition between `from_state` and`to_state` through the `value`

  ```python
  class Transition:
  	def __init__(self, from_state, value, to_state):
  		self.from_state = from_state
  		self.value = value
  		self.to_state = to_state
      
    def accepts(self, value):
  		return self.value == value
  ```

- `RangeTransition`representing a transition between `from_state` and`to_state` through a range of values, ie. `a-z`

  ```python
  class RangeTransition(Transition):
  	def __init__(self, from_state, value, to_state):
  		super(RangeTransition, self).__init__(from_state, value, to_state)
  		self.range = [s.strip() for s in self.value.split("-")]
  
  	def accepts(self, value):
  		return self.range[0] <= value <= self.range[1]
  ```

  

The `Automata` class has a list of `State` objects,  an initial `State`, a list of final `State`objects and a `string` containing the alphabet.

In order to verify if a sequence is accepted, starting from the initial state, we check if a transition can be made to another state using the current character in the sequence. If a transition can be made, we repeat this step until we reach the end of our sequence and we check if the current state is a final state and if so the sequence is accepted. If a transition cannot be made with the current character, the sequence is not accepted.

```python
def accepts(self, string):
	state = self.initial_state
	for character in string:
	   if not state:
	      return False
	   state = self.get_next_node(state, character)

	return state in self.final_states
```



## Integer automata

`input file:`

```c
s0 s1 s2 s3
s0
s2 s3
+-0123456789
s0 -> s1 -
s0 -> s3 0
s3 -> s2 1-9
s0 -> s2 1-9
s1 -> s2 1-9
s2 -> s2 0-9
```

![integer-automata](img/int.svg?raw=true "Integer automata")

## Identifier automata

`input file`

```c
s0 s1 s2
s0
s1 s2
_a-xA-X0-9
s0 -> s1 a-z
s0 -> s1 A-Z
s0 -> s1 _
s0 -> s2 a-z
s0 -> s2 A-Z
s0 -> s2 _
s1 -> s2 a-z
s1 -> s2 A-Z
s1 -> s2 _
s1 -> s2 0-9
s2 -> s2 a-z
s2 -> s2 A-Z
s2 -> s2 _
s2 -> s2 0-9
```

![identifier-automata](img/identif.svg?raw=true "Identifier automata")
