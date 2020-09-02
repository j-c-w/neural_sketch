import argparse
from functools import reduce
import pickle
import sys
import random
random.seed(0)

def test_program_on_IO(e, IO):
    return all(reduce(lambda a, b: a(b), xs, e)==y for xs, y in IO)

def new_list():
    len = random.randint(1, 5)
    res = []
    for x in range(len):
        res.append(new_int())

    return res

def new_int():
    return random.randint(-10, 10)

def generate_new_IO(e, tp, num=10):
    if tp.name == "->" and tp.arguments[1].name == "->":
        args = [tp.arguments[0]] + [tp.arguments[1].arguments[0]]
    elif len(tp.arguments) == 2:
        args = [tp.arguments[0]]

    result_list = []
    for i in range(num):

        if len(args) == 2 and str(args[0]) == "list(int)" and str(args[1]) == "list(int)":
            list1 = new_list()
            list2 = new_list()
            input_args = (list1, list2)

        if len(args) == 2 and str(args[0]) == "list(int)" and str(args[1]) == "int":
            input_args = (new_list(), new_int())
        if len(args) == 2 and str(args[0]) == "int" and str(args[1]) == "list(int)":
            input_args = (new_int(), new_list())

        if len(args) == 1 and str(args[0]) == "int":
            input_args = [new_int()]
        if len(args) == 1 and str(args[0]) == "list(int)":
            input_args = [new_list()]


        result = reduce(lambda a, b: a(b), input_args, e)

        result_list.append([input_args, result])
    return result_list


def regenerate_args(input_file, output_file):
    with open(input_file, 'rb') as f:
        items = pickle.load(f)

    for item in items:
        print (item.tp.arguments)
        converted_types = {}
        e = item.p.evaluate([])
        newIO = generate_new_IO(e, item.tp)
        print ("New IO is ")
        print (newIO)
        if not (test_program_on_IO(e, newIO)):
            print("ERROR! New IO Doesn't match!")
            sys.exit(1)

        item.IO = newIO

    # Now, write to the file:
    with open(output_file, 'wb') as f:
        pickle.dump(items, f)


# The aim of this software is to rerun every component of a 
# pickled results file, and generate some new example
# inputs and outputs for it.

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_pickle')
    parser.add_argument('output_pickle')
    args = parser.parse_args()

    regenerate_args(args.input_pickle, args.output_pickle)
