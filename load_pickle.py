import pickle
import sys

def openfile(file):
    with open(file, 'rb') as f:
        x = pickle.load(f)

    return x

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = sys.argv[1]

file = 'data/T3_test_data_new.p' 
file2 = '/exports/eddie3_homes_local/s1988171/SynthesisEval/synthesis-eval/examples/dot/SketchAdapt'
x = openfile(file)
y = openfile(file2)
