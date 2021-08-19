## SCRIPT BASED ON QUANTUMAI.GOOGLE

from openfermion.hamiltonians import jellium_model
from openfermion.utils import Grid
from openfermion.linalg import eigenspectrum
from openfermion.transforms import jordan_wigner, fourier_transform

##
# Let's look at a very small model of jellium in 1D.
grid = Grid(dimensions=1, length=3, scale=1.0)
spinless = True

##
# Get the momentum Hamiltonian.
momentum_hamiltonian = jellium_model(grid, spinless)
momentum_qubit_operator = jordan_wigner(momentum_hamiltonian)
momentum_qubit_operator.compress()
print('\n momentum_qubit_operator: ',momentum_qubit_operator)

## momentum_qubit_operator:  19.50047638754088 [] +
##-9.71044945799746 [Z0] +
##-0.07957747154594767 [Z0 Z1] +
##-0.07957747154594767 [Z0 Z2] +
##0.15915494309189535 [Z1] +
##-0.07957747154594767 [Z1 Z2] +
##-9.71044945799746 [Z2]

##
# Fourier transform the Hamiltonian to the position basis.
position_hamiltonian = fourier_transform(momentum_hamiltonian, grid, spinless)
position_qubit_operator = jordan_wigner(position_hamiltonian)
position_qubit_operator.compress()
print('\n position_qubit_operator: ', position_qubit_operator)

## position_qubit_operator:  19.500476387540854 [] +
##-3.289868133696451 [X0 X1] +
##-3.289868133696454 [X0 Z1 X2] +
##-3.289868133696451 [Y0 Y1] +
##-3.289868133696454 [Y0 Z1 Y2] +
##-6.420581324301009 [Z0] +
##-0.07957747154594766 [Z0 Z1] +
##-0.07957747154594763 [Z0 Z2] +
##-3.289868133696451 [X1 X2] +
##-3.289868133696451 [Y1 Y2] +
##-6.4205813243010095 [Z1] +
##-0.07957747154594766 [Z1 Z2] +
##-6.420581324301009 [Z2]

##
# Check the spectra to make sure these representations are iso-spectral.
spectral_difference = eigenspectrum(momentum_qubit_operator) -  eigenspectrum(position_qubit_operator)
print('\n spectral_difference: ', spectral_difference)

## spectral_difference:  [2.75474088e-14 2.66175970e-14 2.84217094e-14 7.10542736e-15
## 2.84217094e-14 2.13162821e-14 1.42108547e-14 7.10542736e-15]

