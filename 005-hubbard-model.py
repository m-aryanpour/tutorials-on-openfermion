## SCRIPT BASED ON QUANTUMAI.GOOGLE

from openfermion.hamiltonians import fermi_hubbard
from openfermion.linalg import get_sparse_operator, get_ground_state
from openfermion.transforms import jordan_wigner

##
# Set model.
x_dimension = 2
y_dimension = 2
tunneling   = 2.
coulomb     = 1.
periodic    = 1
spinless    = 1
magnetic_field     = 0.5
chemical_potential = 0.25

# Get fermion operator.
hubbard_model = fermi_hubbard(
    x_dimension, y_dimension, tunneling, coulomb, chemical_potential,
    magnetic_field, periodic, spinless)
print('\n hubbard model: ', hubbard_model)

## hubbard model:  -0.25 [0^ 0] +
##1.0 [0^ 0 1^ 1] +
##1.0 [0^ 0 2^ 2] +
##-2.0 [0^ 1] +
##-2.0 [0^ 2] +
##-2.0 [1^ 0] +
##-0.25 [1^ 1] +
##1.0 [1^ 1 3^ 3] +
##-2.0 [1^ 3] +
##-2.0 [2^ 0] +
##-0.25 [2^ 2] +
##1.0 [2^ 2 3^ 3] +
##-2.0 [2^ 3] +
##-2.0 [3^ 1] +
##-2.0 [3^ 2] +
##-0.25 [3^ 3]

##
# Get qubit operator under Jordan-Wigner.
jw_hamiltonian = jordan_wigner(hubbard_model)
jw_hamiltonian.compress()
print('\n jw_hamiltonian: ', jw_hamiltonian)

## jw_hamiltonian:  0.5 [] +
##-1.0 [X0 X1] +
##-1.0 [X0 Z1 X2] +
##-1.0 [Y0 Y1] +
##-1.0 [Y0 Z1 Y2] +
##-0.375 [Z0] +
##0.25 [Z0 Z1] +
##0.25 [Z0 Z2] +
##-1.0 [X1 Z2 X3] +
##-1.0 [Y1 Z2 Y3] +
##-0.375 [Z1] +
##0.25 [Z1 Z3] +
##-1.0 [X2 X3] +
##-1.0 [Y2 Y3] +
##-0.375 [Z2] +
##0.25 [Z2 Z3] +
##-0.375 [Z3]

##
# Get scipy.sparse.csc representation.
sparse_operator = get_sparse_operator(hubbard_model)
print('\n sparse_operator: ', sparse_operator)

## sparse_operator:    (1, 1)	(-0.25+0j)
##  (2, 1)	(-2+0j)
##  (4, 1)	(-2+0j)
##  (1, 2)	(-2+0j)
##  (2, 2)	(-0.25+0j)
##  (8, 2)	(-2+0j)
##  (3, 3)	(0.5+0j)
##  (6, 3)	(2+0j)
##  (9, 3)	(-2+0j)
##  (1, 4)	(-2+0j)
##  (4, 4)	(-0.25+0j)
##  (8, 4)	(-2+0j)
##  (5, 5)	(0.5+0j)
##  (6, 5)	(-2+0j)
##  (9, 5)	(-2+0j)
##  (3, 6)	(2+0j)
##  (5, 6)	(-2+0j)
##  (6, 6)	(-0.5+0j)
##  (10, 6)	(-2+0j)
##  (12, 6)	(2+0j)
##  (7, 7)	(1.25+0j)
##  (11, 7)	(-2+0j)
##  (13, 7)	(2+0j)
##  (2, 8)	(-2+0j)
##  (4, 8)	(-2+0j)
##  (8, 8)	(-0.25+0j)
##  (3, 9)	(-2+0j)
##  (5, 9)	(-2+0j)
##  (9, 9)	(-0.5+0j)
##  (10, 9)	(-2+0j)
##  (12, 9)	(-2+0j)
##  (6, 10)	(-2+0j)
##  (9, 10)	(-2+0j)
##  (10, 10)	(0.5+0j)
##  (7, 11)	(-2+0j)
##  (11, 11)	(1.25+0j)
##  (14, 11)	(2+0j)
##  (6, 12)	(2+0j)
##  (9, 12)	(-2+0j)
##  (12, 12)	(0.5+0j)
##  (7, 13)	(2+0j)
##  (13, 13)	(1.25+0j)
##  (14, 13)	(-2+0j)
##  (11, 14)	(2+0j)
##  (13, 14)	(-2+0j)
##  (14, 14)	(1.25+0j)
##  (15, 15)	(3+0j)
##

##
Energy = get_ground_state(sparse_operator)[0]
print('\nEnergy of the model is {} in units of T and J.'.format(Energy))

##Energy of the model is -4.250000000000001 in units of T and J.


