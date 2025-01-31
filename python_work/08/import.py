import printing_functions
from printing_functions import print_models
from printing_functions import print_models as pm
import printing_functions as pf
from printing_functions import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
complated_models = []

printing_functions.print_models(unprinted_designs[:], complated_models)
print_models(unprinted_designs[:], complated_models)
pm(unprinted_designs[:], complated_models)

# 传递列表的副本
pf.print_models(unprinted_designs[:], complated_models)
show_complated_models(complated_models)
