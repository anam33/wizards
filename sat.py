import argparse
import networkx as nx
import random
import matplotlib.pyplot as plt
from networkx.utils import arbitrary_element
from satispy import Variable, Cnf 
from satispy.solver import Minisat


def poo():
	solver = Minisat()
	AB = Variable('ab')
	AC = Variable('ac')
	BA = Variable('ba')
	BC = Variable('bc')
	CA = Variable('ca')
	CB = Variable('cb')

	exp = (AB & AC & BC) ^ (AB & CA & CB) ^ (AC & BA & BC) ^ (BA & CA & CB)

	solution = solver.solve(exp)

	if solution.success:
		print(solution[AB])
		print(solution[AC])
		print(solution[AB]) 
		print(solution[AB])
		print(solution[AB])
		print(solution[AB])

poo()