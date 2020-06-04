This is a set of instructions to get this thing working on Eddie.

# Building the model
Needs to be done on an Eddie GPU instance: qlogin -l h_vmem=8G -pe gpu 1

run to install it.
> ./install.sh

Then execute the output line that sets up the python environment.

They run:
./retrain.sh <some dir in the exports>

That does the main training thing.


Then there are the sub training options, which you get to  by doing some
stuff in the main README.

# Running the Model
You need the dependencies in ./install.sh, and pypy3.

Don't just run install.sh though, that's built for the cluster.  Have
a look in there to see what it installs.

There's a script called ./install_eval.sh that that installs
a pypy locally for a non-cluster machine, so you can take a
look at that.


# Errors
if you get some errors about nvidia drivers not being compatible,
try making sure that torch==1.4.0 is installed

can also try:
try running nvidia-smi and checking the cuda version.
