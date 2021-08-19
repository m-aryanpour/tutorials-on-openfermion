## SCRIPT BASED ON QUANTUMAI.GOOGLE
from openfermion.chem import MolecularData
from openfermion.transforms import get_fermion_operator, jordan_wigner
from openfermion.linalg import get_ground_state, get_sparse_operator
import numpy
import scipy
import scipy.linalg

##
# Load saved file for LiH.
diatomic_bond_length = 1.45
geometry = [('Li', (0., 0., 0.)), ('H', (0., 0., diatomic_bond_length))]
basis = 'sto-3g'
multiplicity = 1

# Set Hamiltonian parameters.
active_space_start = 1
active_space_stop = 3

# Generate and populate instance of MolecularData.
molecule = MolecularData(geometry, basis, multiplicity, description="1.45")
molecule.load()

##
# Get the Hamiltonian in an active space.
molecular_hamiltonian = molecule.get_molecular_hamiltonian(
    occupied_indices=range(active_space_start),
    active_indices=range(active_space_start, active_space_stop))

##
# Map operator to fermions and qubits.
fermion_hamiltonian = get_fermion_operator(molecular_hamiltonian)
qubit_hamiltonian = jordan_wigner(fermion_hamiltonian)
qubit_hamiltonian.compress()
print('The Jordan-Wigner Hamiltonian in canonical basis follows:\n{}'.format(qubit_hamiltonian))

##The Jordan-Wigner Hamiltonian in canonical basis follows:
##-7.49894690201071 [] +
##-0.0029329964409502266 [X0 X1 Y2 Y3] +
##0.0029329964409502266 [X0 Y1 Y2 X3] +
##0.01291078027311749 [X0 Z1 X2] +
##-0.0013743761078958677 [X0 Z1 X2 Z3] +
##0.011536413200774975 [X0 X2] +
##0.0029329964409502266 [Y0 X1 X2 Y3] +
##-0.0029329964409502266 [Y0 Y1 X2 X3] +
##0.01291078027311749 [Y0 Z1 Y2] +
##-0.0013743761078958677 [Y0 Z1 Y2 Z3] +
##0.011536413200774975 [Y0 Y2] +
##0.16199475388004184 [Z0] +
##0.011536413200774975 [Z0 X1 Z2 X3] +
##0.011536413200774975 [Z0 Y1 Z2 Y3] +
##0.12444770133137588 [Z0 Z1] +
##0.054130445793298836 [Z0 Z2] +
##0.05706344223424907 [Z0 Z3] +
##0.012910780273117487 [X1 Z2 X3] +
##-0.0013743761078958677 [X1 X3] +
##0.012910780273117487 [Y1 Z2 Y3] +
##-0.0013743761078958677 [Y1 Y3] +
##0.16199475388004186 [Z1] +
##0.05706344223424907 [Z1 Z2] +
##0.054130445793298836 [Z1 Z3] +
##-0.013243698330265966 [Z2] +
##0.08479609543670981 [Z2 Z3] +
##-0.013243698330265952 [Z3]

##
# Get sparse operator and ground state energy.
sparse_hamiltonian = get_sparse_operator(qubit_hamiltonian)
energy, state = get_ground_state(sparse_hamiltonian)
print('Ground state energy before rotation is {} Hartree.\n'.format(energy))

##Ground state energy before rotation is -7.862773163027991 Hartree.

##
# Randomly rotate.
n_orbitals = molecular_hamiltonian.n_qubits // 2
n_variables = int(n_orbitals * (n_orbitals - 1) / 2)
numpy.random.seed(1)
random_angles = numpy.pi * (1. - 2. * numpy.random.rand(n_variables))
kappa = numpy.zeros((n_orbitals, n_orbitals))
index = 0
for p in range(n_orbitals):
    for q in range(p + 1, n_orbitals):
        kappa[p, q] = random_angles[index]
        kappa[q, p] = -numpy.conjugate(random_angles[index])
        index += 1

    # Build the unitary rotation matrix.
    difference_matrix = kappa + kappa.transpose()
    rotation_matrix = scipy.linalg.expm(kappa)

    # Apply the unitary.
    molecular_hamiltonian.rotate_basis(rotation_matrix)

# Get qubit Hamiltonian in rotated basis.
qubit_hamiltonian = jordan_wigner(molecular_hamiltonian)
qubit_hamiltonian.compress()
print('The Jordan-Wigner Hamiltonian in rotated basis follows:\n{}'.format(qubit_hamiltonian))

##The Jordan-Wigner Hamiltonian in rotated basis follows:
##-7.498946902010708 [] +
##-0.02426005446824693 [X0 X1 Y2 Y3] +
##0.02426005446824693 [X0 Y1 Y2 X3] +
##-0.08262397170394278 [X0 Z1 X2] +
##-0.016734989174013625 [X0 Z1 X2 Z3] +
##-0.005524724636333802 [X0 X2] +
##0.02426005446824693 [Y0 X1 X2 Y3] +
##-0.02426005446824693 [Y0 Y1 X2 X3] +
##-0.08262397170394278 [Y0 Z1 Y2] +
##-0.016734989174013625 [Y0 Z1 Y2 Z3] +
##-0.005524724636333802 [Y0 Y2] +
##0.04248358003893321 [Z0] +
##-0.0055247246363338024 [Z0 X1 Z2 X3] +
##-0.0055247246363338024 [Z0 Y1 Z2 Y3] +
##0.0823812751073221 [Z0 Z1] +
##0.05413044579329885 [Z0 Z2] +
##0.07839050026154579 [Z0 Z3] +
##-0.08262397170394278 [X1 Z2 X3] +
##-0.016734989174013625 [X1 X3] +
##-0.08262397170394278 [Y1 Z2 Y3] +
##-0.016734989174013625 [Y1 Y3] +
##0.042483580038933204 [Z1] +
##0.07839050026154579 [Z1 Z2] +
##0.05413044579329885 [Z1 Z3] +

# Get sparse Hamiltonian and energy in rotated basis.
sparse_hamiltonian = get_sparse_operator(qubit_hamiltonian)
energy, state = get_ground_state(sparse_hamiltonian)
print('Ground state energy after rotation is {} Hartree.'.format(energy))

##Ground state energy after rotation is -7.862773163027994 Hartree.
