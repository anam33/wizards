import argparse
import networkx as nx
import random
import matplotlib.pyplot as plt
from networkx.utils import arbitrary_element
from satispy import Variable, Cnf 
from satispy.solver import Minisat


def poo():
	solver = Minisat()
	AB = Variable('AB')
	AC = Variable('AC')
	BA = Variable('BA')
	BC = Variable('BC')
	CA = Variable('CA')
	CB = Variable('CB')

	exp = (AB & AC & BC) | (AB & CA & CB) | (BA & AC & BC) | (BA & CA & CB) & (AB ^ BA) & (AC ^ CA) & (CB ^ BC)

	exp = exp & BA
	# (A & B & D) | (A & E & F) | (B & C & D) | (C & E & F) & (A ^ C) & (B ^ E) & (F ^ D)
	# (AB & AC & BC) ^ (AB & CA & CB) ^ (AC & BA & BC) ^ (BA & CA & CB)

	solution = solver.solve(exp)

	if solution.success:
		print(solution[AB])
		print(solution[AC])
		print(solution[BA]) 
		print(solution[BC])
		print(solution[CA])
		print(solution[CB])

poo()