# Released to students

import sys

def main(argv):
    if len(argv) != 2:
        print("Usage: python instance_validator.py [path_to_input_file] [20, 35 or 50]")
        return
    if (int(argv[1]) not in [20, 35, 50]):
        print("The final argument must be 20, 35 or 50.")
    print(processInput(argv[0], int(argv[1])))

def processInput(s, max_nodes):
    fin = open(s, "r")
    line1 = fin.readline().split()
    # Ensures that the first line contains an integer.
    if len(line1) != 1 or not line1[0].isdigit():
        return "Line 1 must contain a single integer, which is the total number of wizards at the party."

    # Ensures that the number of objects are between 1 and 50.
    N = int(line1[0])
    if N < 1 or N > max_nodes:
        return "N must be an integer between 1 and {max_nodes}, inclusive.".format(max_nodes=max_nodes)

    # Ensures that line 1 and line 2 agree.
    line2 = fin.readline().split()
    if (len(line2) != N):
        return "Number of wizards present doesn't match the number of wizards in line 1. Line 1 says there are {} wizards, but line 2 contains {} wizards".format(N, len(line2))

    # Sets and maps for ensuring validity
    node_set = set(line2)
    node_map = {k: v for v, k in enumerate(line2)}

    # Makes sure all wizards are unique
    if (len(node_set) != len(line2)):
        return "Wizards cannot appear multiple times in the perfect age ordering. There are {} total wizards, but only {} unique wizards in the perfect ordering.".format(len(line2), len(node_set))

    # Makes sure wizard names are alnum and < 10 characters long
    for wizard in node_set:
        if not wizard.isalnum() or len(wizard) > 10:
            return "Wizards' names must be alphanumeric, and at most 10 characters long."

    # MAkes sure that line 3 is a number between 1 and 500
    line3 = fin.readline().split()
    if len(line3) != 1 or not line3[0].isdigit():
        return "Line 3 must contain a single integer, which is the total number of age constraints you've heard at the party."

    num_constraints = int(line3[0])
    if (num_constraints < 1 or num_constraints > 500):
        return "You must have heard between 1 and 500 (inclusive) age constraints at the party."

    # Makes sure that all the constraints match up with the provided perfect ordering.
    for i in range(num_constraints):
        line_num = i + 4
        constraint = fin.readline().split()
        if (len(constraint) != 3):
            return "Each constraint must have 3 wizards. Line {} (1-index) does not contain 3 wizards".format(line_num)
        if not set(constraint).issubset(node_set):
            return "Some of the wizards in line {} are not present in the perfect age ordering.".format(line_num)

        wiz_a = node_map[constraint[0]]
        wiz_b = node_map[constraint[1]]
        wiz_mid = node_map[constraint[2]]

        if (wiz_a < wiz_mid < wiz_b) or (wiz_b < wiz_mid < wiz_a):
            return "In line {i}, you said {wizard_mid}'s age was NOT in between {wizard_a} and {wizard_b}'s, however, in your optimal ordering, {wizard_a} appeared at {a_order}, {wizard_b} appeared at {b_order}, {wizard_mid} appeared at {mid_order}".format(i = line_num, wizard_a = constraint[0], wizard_b = constraint[1], wizard_mid = constraint[2], a_order = wiz_a, b_order = wiz_b, mid_order = wiz_mid)
            

    # Checks that there are no lines after the number of constraints are exhausted
    if fin.readline().split() != []:
        return "You said that there were {} constraints, but there was more input in the lines below that".format(num_constraints)

    return("Success!")

if __name__ == '__main__':
    main(sys.argv[1:])
