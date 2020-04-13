# https://en.wikipedia.org/wiki/Qiskit
# https://qiskit.org/terra

from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])

backend = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, backend)
sim_result = job_sim.result()

print(sim_result.get_counts(qc))
