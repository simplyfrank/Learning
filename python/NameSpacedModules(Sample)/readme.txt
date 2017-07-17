Demonstrates how a module can be imported from two distinct pathes in Python automatically.

In order for this to work, both paths must be appended to the system path like so:

import sys

sys.path.extend(['path1', 'path2'])

import split_farm
from split_farm import bovine
from spit_farm import birds