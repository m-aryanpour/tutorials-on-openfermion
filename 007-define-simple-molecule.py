## SCRIPT BASED ON QUANTUMAI.GOOGLE

from openfermion.chem import MolecularData
import numpy as np

##
# Set parameters to make a simple molecule.

OH= 0.75
th = np.deg2rad(105.)
cs, sn = np.cos(th), np.sin(th)
geometry = [('O', (0., 0., 0.)),
            ('H', (OH, 0., 0.)),
            ('H', (OH*cs, OH*sn, 0.))]
basis        = 'sto-3g'
multiplicity = 1
charge       = 0
description  = str('H2O molecule')

##
# Make molecule and print out a few interesting facts about it.
molecule = MolecularData(geometry, basis, multiplicity,
                         charge, description)
print('Molecule has automatically generated name {}'.format(
    molecule.name))
print('Information about this molecule would be saved at:\n{}\n'.format(
    molecule.filename))
print('This molecule has {} atoms and {} electrons.'.format(
    molecule.n_atoms, molecule.n_electrons))
for atom, atomic_number in zip(molecule.atoms, molecule.protons):
    print('Contains {} atom, which has {} protons.'.format(
        atom, atomic_number))

##Molecule has automatically generated name H2-O1_sto-3g_singlet_H2O molecule
##Information about this molecule would be saved at:
##data/H2-O1_sto-3g_singlet_H2O molecule
##
##This molecule has 3 atoms and 10 electrons.
##Contains H atom, which has 1 protons.
##Contains H atom, which has 1 protons.
##Contains O atom, which has 8 protons.
