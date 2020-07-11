#https://medium.com/qiskit/this-proof-demonstrates-a-quantum-advantage-even-for-noisy-quantum-computers-b44a738801ad
#https://gist.github.com/ryanfmandelbaum/a174f044dddec988baea90222c1b0457#file-magic_square-py
from qiskit import *
#The following function sets up the initial entanglement between Alice and Bob
def share_bell_state(qc,a,b,c,d): 
    qc.h(a)
    qc.h(b)
    qc.cx(a,c)
    qc.cx(b,d)
    
#The following functions represent the U(gamma) and V(gamma) controlled Cliffords.
def U(qc,gamma,a,b):
    if gamma==1:
        qc.h(a)
        qc.i(b)
    
    elif gamma==2:
        qc.h(a)
        qc.i(b)
        qc.swap(a,b)
    
    elif gamma==3:
        qc.h(a)
        qc.i(b)
        qc.cx(a,b)
    
def V(qc,gamma,a,b):
    if gamma==1:
        qc.h(a)
        qc.h(b)
    
    if gamma==2:
        qc.swap(a,b)
    
    elif gamma==3:
        qc.h(a)
        qc.h(b)
        qc.cz(a,b)
        qc.z(a)
        qc.z(b)

#We will ask the user to select the row and column on Alice and Bob's behalf.
print("Alice and Bob, select a column or row value of 1, 2, or 3") 
print("Alice choice (column):")
alpha = int(input())
print("Bob choice (row):")
beta = int(input())

#Create the quantum register and the classical register to store our final bit values
aliceQR = QuantumRegister(2)
x1CR = ClassicalRegister(1)
x2CR = ClassicalRegister(1)
bobQR = QuantumRegister(2)
y1CR = ClassicalRegister(1)
y2CR = ClassicalRegister(1)

#Create the circuit
magicsquare_circuit = QuantumCircuit(aliceQR,bobQR,x1CR,x2CR,y1CR,y2CR)

#Generate the Bell state on the circuit
share_bell_state(magicsquare_circuit,0,1,2,3)

magicsquare_circuit.barrier()

#Draw the rest of the circuit based on Alice and Bob's selection   
if 4>alpha>0 and 4>beta>0:
    U(magicsquare_circuit,alpha,0,1) 
    V(magicsquare_circuit,beta,2,3)
    magicsquare_circuit.measure(0,0)
    magicsquare_circuit.measure(1,1)
    magicsquare_circuit.measure(2,2)
    magicsquare_circuit.measure(3,3)
   
else:
    print("please enter values of 1, 2, or 3")
