## SCRIPT BASED ON QUANTUMAI.GOOGLE

from openfermion.ops import FermionOperator

## sum of terms
term_1 = FermionOperator('4^ 3^ 9 1', 1. + 2.j)
term_2 = FermionOperator('3^ 1', -1.7)
operator1 = term_1 + term_2
print('operator1:',operator1)

operator2 = FermionOperator('4^ 3^ 9 1', 1. + 2.j)
term_2    = FermionOperator('3^ 1', -1.7)
operator2 += term_2
print('operator2= ', operator2)

##operator1: -1.7 [3^ 1] +
##(1+2j) [4^ 3^ 9 1]
##operator2=  -1.7 [3^ 1] +
##(1+2j) [4^ 3^ 9 1]



## more builtin operations on terms
term_1 = FermionOperator('4^ 3^ 9 1', 1. + 2.j)
term_2 = FermionOperator('3^ 1', -1.7)

operator1 = term_1 - 33. * term_2
print('\n operator1= ', operator1)

operator1 *= 3.17 * (term_2 + term_1) ** 2
print('\n now operator1= ', operator1)


print('\n term_2**3 = ', term_2 ** 3)

print('\n boolean: term_1 =?= 2.*term_1 - term_1-> ', term_1 == 2.*term_1 - term_1)
print('\n boolean: term_1 =?= operator1 -> ', term_1 == operator1)

## operator1=  56.1 [3^ 1] +
##(1+2j) [4^ 3^ 9 1]
##
## now operator1=  513.9489299999999 [3^ 1 3^ 1 3^ 1] +
##(-302.32289999999995-604.6457999999999j) [3^ 1 3^ 1 4^ 3^ 9 1] +
##(-302.32289999999995-604.6457999999999j) [3^ 1 4^ 3^ 9 1 3^ 1] +
##(-533.511+711.348j) [3^ 1 4^ 3^ 9 1 4^ 3^ 9 1] +
##(9.161299999999999+18.322599999999998j) [4^ 3^ 9 1 3^ 1 3^ 1] +
##(16.166999999999998-21.555999999999997j) [4^ 3^ 9 1 3^ 1 4^ 3^ 9 1] +
##(16.166999999999998-21.555999999999997j) [4^ 3^ 9 1 4^ 3^ 9 1 3^ 1] +
##(-34.87-6.34j) [4^ 3^ 9 1 4^ 3^ 9 1 4^ 3^ 9 1]
##
## term_2**3 =  -4.912999999999999 [3^ 1 3^ 1 3^ 1]
##
## boolean: term_1 =?= 2.*term_1 - term_1->  True
##
## boolean: term_1 =?= operator1 ->  False

## EVEN MORE OPERATIONS
from openfermion.utils import commutator, count_qubits, hermitian_conjugated
from openfermion.transforms import normal_ordered

# Get the Hermitian conjugate of a FermionOperator, count its qubit, check if it is normal-ordered.
term_1 = FermionOperator('4^ 3 3^', 1. + 2.j)
print(' term_1= ',term_1)
print(' hermitian_conjugated(term_1)= ', hermitian_conjugated(term_1))
print(' term_1.is_normal_ordered()= ', term_1.is_normal_ordered())
print(' count_qubits(term_1)= ',count_qubits(term_1))

# Normal order the term.
term_2 = normal_ordered(term_1)
print(' term_2= normal_ordered(term_1)= ',term_2)

# Compute a commutator of the terms.
print('')
print(' commutator(term_1, term_2)= ',commutator(term_1, term_2))

## term_1=  (1+2j) [4^ 3 3^]
## hermitian_conjugated(term_1)=  (1-2j) [3 3^ 4]
## term_1.is_normal_ordered()=  False
## count_qubits(term_1)=  5
## term_2= normal_ordered(term_1)=  (1+2j) [4^] +
##(-1-2j) [4^ 3^ 3]
##
## commutator(term_1, term_2)=  (-3+4j) [4^ 3 3^ 4^] +
##(3-4j) [4^ 3 3^ 4^ 3^ 3] +
##(-3+4j) [4^ 3^ 3 4^ 3 3^] +
##(3-4j) [4^ 4^ 3 3^]
