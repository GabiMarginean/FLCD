from automata import Automata


def verify_accepts(a):
	print("")
	seq = input("sequence: ")
	print(a.accepts(seq))


actions = {
"1" : Automata.states,
"2" : Automata.alphabet,
"3" : Automata.transitions,
"4" : Automata.final_states,
"5" : verify_accepts
}



def printMenu():
	print("1. Set of states\n2. Alphabet\n3. Transitions\n4. Final states\n5. Accepts\n0. Exit")



if __name__ == '__main__':
	a = Automata("int_FA.in")
	while(True):
		printMenu()

		option = input(">> ")

		if option == "0":
			break

		if option in actions:
			actions[option](a)
		else:
			print("Invalid option")