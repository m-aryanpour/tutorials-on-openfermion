## SCRIPT BASED ON QUANTUMAI.GOOGLE

from openfermion.ops import FermionOperator
from openfermion.transforms import jordan_wigner, bravyi_kitaev
from openfermion.utils import hermitian_conjugated
from openfermion.linalg import eigenspectrum
##
# Initialize an operator.
fermion_operator = FermionOperator('2^ 0', 3.17)
fermion_operator += hermitian_conjugated(fermion_operator)
print('\n fermion-operator:',fermion_operator)

## fermion-operator: 3.17 [0^ 2] +
##3.17 [2^ 0]

##
# Transform to qubits under the Jordan-Wigner transformation and print its spectrum.
jw_operator = jordan_wigner(fermion_operator)
print('')
print('\n jw_operator:' ,jw_operator)
jw_spectrum = eigenspectrum(jw_operator)
print('\n jw_spectrum: ',jw_spectrum)

## jw_operator: (1.585+0j) [X0 Z1 X2] +
##(1.585+0j) [Y0 Z1 Y2]
##
## jw_spectrum:  [-3.17 -3.17  0.    0.    0.    0.    3.17  3.17]

##
# Transform to qubits under the Bravyi-Kitaev transformation and print its spectrum.
bk_operator = bravyi_kitaev(fermion_operator)
print('\n bk_operator: ', bk_operator)
bk_spectrum = eigenspectrum(bk_operator)
print('\n bk_spectrum: ',bk_spectrum)

## bk_operator:  (1.585+0j) [X0 Y1 Y2] +
##(-1.585+0j) [Y0 Y1 X2]
##
## bk_spectrum:  [-3.17 -3.17  0.    0.    0.    0.    3.17  3.17]

##
from openfermion.transforms import reverse_jordan_wigner

# Initialize QubitOperator.
operator1 = QubitOperator('X0 Y1 Z2', 88.)
operator1 += QubitOperator('Z1 Z4', 3.17)
print('\n operator1: ',operator1)

# Map QubitOperator to a FermionOperator.
mapped_operator = reverse_jordan_wigner(operator1)
print('\n mapped_operator: ', mapped_operator)

# Map the operator back to qubits and make sure it is the same.
back_to_normal = jordan_wigner(mapped_operator)
back_to_normal.compress()
print('\n back_to_normal: ', back_to_normal)

## operator1:  88.0 [X0 Y1 Z2] +
##3.17 [Z1 Z4]
##
## mapped_operator:  3.17 [] +
##-88j [1 0] +
##88j [1 0^] +
##88j [1^ 0] +
##-88j [1^ 0^] +
##-6.34 [1^ 1] +
##176j [2^ 2 1 0] +
##-176j [2^ 2 1 0^] +
##-176j [2^ 2 1^ 0] +
##176j [2^ 2 1^ 0^] +
##-6.34 [4^ 4] +
##12.68 [4^ 4 1^ 1]
##
## back_to_normal:  88.0 [X0 Y1 Z2] +
##3.17 [Z1 Z4]
