## SCRIPT BASED ON QUANTUMAI.GOOGLE

from openfermion.ops import FermionOperator

## different ways to initialize operators
term1 = FermionOperator(((3,1), (1,0)))
print('term1= ',term1)

term2 = FermionOperator('3^ 1')
print('term2= ',term2)

##term1=  1.0 [3^ 1]
##term2=  1.0 [3^ 1]

## good/bad/ugly ways to initialize operators
good_way_to_initialize = FermionOperator('3^ 1', -1.7)
print('good way to initialize:', good_way_to_initialize)

bad_way_to_initialize = -1.7 * FermionOperator('3^ 1')
print('bad way to initialize:' ,bad_way_to_initialize)

identity = FermionOperator('')
print('identity:', identity)

zero_operator = FermionOperator()
print('zero operator: ', zero_operator)

##good way to initialize: -1.7 [3^ 1]
##bad way to initialize: -1.7 [3^ 1]
##identity: 1.0 []
##zero operator:  0

## terms in an operator
operator1 = FermionOperator('4^ 1^ 3 9', 1. + 2.j)
print(operator1)
print('operator terms:' , operator1.terms)

##(1+2j) [4^ 1^ 3 9]
##operator terms: {((4, 1), (1, 1), (3, 0), (9, 0)): (1+2j)}
