# Runs optimise 

from sys import argv
from optimise import run_through_optimisations

tpd_file = argv[1]

run_through_optimisations(tpd_file, print_all_images=True)
