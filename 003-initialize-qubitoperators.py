## SCRIPT BASED ON QUANTUMAI.GOOGLE

from openfermion.ops import QubitOperator

## sum of terms
qubit_operator1 = QubitOperator('X1 Y2 Z3')
print('quibit-operator1:',  qubit_operator1)
print('qubit_operator1.terms: ', qubit_operator1.terms)

operator2  = QubitOperator('X3 Z4', 3.17)
operator2 -= 77. * qubit_operator1
print(' operator2: ', operator2)

##quibit-operator1: 1.0 [X1 Y2 Z3]
##qubit_operator1.terms:  {((1, 'X'), (2, 'Y'), (3, 'Z')): 1.0}
## operator2:  -77.0 [X1 Y2 Z3] +
##3.17 [X3 Z4]
