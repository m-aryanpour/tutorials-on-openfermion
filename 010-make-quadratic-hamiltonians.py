## SCRIPT BASED ON QUANTUMAI.GOOGLE

from openfermion.hamiltonians import mean_field_dwave
from openfermion.transforms import get_quadratic_hamiltonian

##
# Set model.
x_dimension = 2
y_dimension = 2
tunneling   = 2.
sc_gap      = 1.
periodic   = True

##
# Get FermionOperator.
mean_field_model = mean_field_dwave(
    x_dimension, y_dimension, tunneling, sc_gap, periodic=periodic)
##
# Convert to QuadraticHamiltonian
quadratic_hamiltonian = get_quadratic_hamiltonian(mean_field_model)
##
# Compute the ground energy
ground_energy = quadratic_hamiltonian.ground_energy()
print('\n ground state energy: ', ground_energy)

##ground state energy:  -9.99999999999999


##
orbital_energies, constant = quadratic_hamiltonian.orbital_energies()
print('\n orbital_energies: ',orbital_energies)
print('\n constants: ', constant)

## orbital_energies:  [1. 1. 1. 1. 4. 4. 4. 4.]
##
## constants:  -9.99999999999999

##
from openfermion.circuits import gaussian_state_preparation_circuit

circuit_description, start_orbitals = gaussian_state_preparation_circuit(quadratic_hamiltonian)
for ip, parallel_ops in enumerate(circuit_description):
    print(f"{ip}: parallel_ops= ", parallel_ops)
print('\n start_orbitals: ',start_orbitals )

##0: parallel_ops=  ('pht',)
##1: parallel_ops=  ((6, 7, 1.5707963267948966, 0.0),)
##2: parallel_ops=  ('pht', (5, 6, 1.5707963267948966, 0.0))
##3: parallel_ops=  ((4, 5, 1.0471975511965979, 3.141592653589792), (6, 7, 1.0471975511965976, -3.1415926535897927))
##4: parallel_ops=  ('pht', (3, 4, 1.5707963267948966, 0.0), (5, 6, 1.5707963267948966, 0.0))
##5: parallel_ops=  ((2, 3, 1.2309594173407747, -5.051514762044463e-15), (4, 5, 1.230959417340775, -6.661338147750939e-16), (6, 7, 1.1071487177940904, -3.141592653589792))
##6: parallel_ops=  ('pht', (1, 2, 1.5707963267948966, 0.0), (3, 4, 1.5707963267948966, 0.0), (5, 6, 1.5707963267948966, 0.0))
##7: parallel_ops=  ((0, 1, 1.0471975511965983, -3.141592653589793), (2, 3, 1.0471975511965976, 3.141592653589792), (4, 5, 1.3181160716528177, -3.1415926535897905), (6, 7, 1.3181160716528177, -2.220446049250313e-16))
##8: parallel_ops=  ('pht', (1, 2, 1.5707963267948966, 0.0), (3, 4, 1.5707963267948966, 0.0), (5, 6, 1.5707963267948966, 0.0))
##9: parallel_ops=  ((2, 3, 0.955316618124509, 6.66133814775094e-16), (4, 5, 0.9553166181245096, 4.440892098500627e-16), (6, 7, 1.1071487177940906, 0.0))
##10: parallel_ops=  ('pht', (3, 4, 1.5707963267948966, 0.0), (5, 6, 1.5707963267948966, 0.0))
##11: parallel_ops=  ((4, 5, 0.7853981633974485, 3.1415926535897927), (6, 7, 0.7853981633974481, 1.1102230246251567e-15))
##12: parallel_ops=  ((5, 6, 1.5707963267948966, 0.0),)
##
## start_orbitals:  []
