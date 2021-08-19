## SCRIPT BASED ON QUANTUMAI.GOOGLE

from openfermion.chem import MolecularData
import numpy as np
##
# Set molecule parameters.
basis        = 'sto-3g'
multiplicity = 1
n_points     = 25
bond_length_interval = 0.1

##
# Generate molecule at different bond lengths.
hf_energies  = []
fci_energies = []
mp2_energies = []
bond_lengths = []
Header= 'bond-length   HF-energy   MP2-energy  FCI-energy  nuclear-repulsion  orbital1-energy   orbital2-energy'
Format = "  ".join(["%8.5f " for i in Header.split()])
print(Header)
for point in range(3, n_points + 1):
    bond_length = bond_length_interval * point
    bond_lengths += [bond_length]
    description = str(round(bond_length,2))
    geometry = [('H', (0., 0., 0.)), ('H', (0., 0., bond_length))]
    molecule = MolecularData(
        geometry, basis, multiplicity, description=description)

    # Load data.
    molecule.load()

    # Print out some results of calculation.
    
    print(Format % (bond_length, molecule.hf_energy, molecule.mp2_energy,
          molecule.fci_energy, molecule.nuclear_repulsion,
          molecule.orbital_energies[0], molecule.orbital_energies[1]))

    hf_energies += [molecule.hf_energy]
    fci_energies += [molecule.fci_energy]
    mp2_energies += [molecule.mp2_energy]

# Plot.
import matplotlib.pyplot as plt


plt.figure(0)
plt.plot(bond_lengths, fci_energies, 'x-')
plt.plot(bond_lengths, hf_energies, 'o-')
plt.plot(bond_lengths, mp2_energies, 's-')
plt.ylabel('Energy in Hartree')
plt.xlabel('Bond length in angstrom')
plt.legend(['HF','FCI','MP2'])
plt.grid()
plt.show()
