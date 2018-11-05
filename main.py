import numpy as np
from confusion_matrix import print_conf_mat
from performance_parameters import print_per_para



M = ([[23, 23,  6],
       [ 9,  5,  8],
       [25, 27, 28]])

print_conf_mat(M)
print_per_para(M)