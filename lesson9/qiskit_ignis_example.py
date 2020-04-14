import qiskit
from qiskit.providers.aer.noise import NoiseModel
from qiskit.providers.aer.noise.errors.standard_errors import depolarizing_error

# Import the RB Functions
from qiskit.ignis.verification.randomized_benchmarking import randomized_benchmarking_seq, RBFitter

# Generate RB circuits (2Q RB)
rb_opts = {}
rb_opts['length_vector'] = [1, 10, 20, 50, 75, 100, 125]
rb_opts['nseeds'] = 5
rb_opts['rb_pattern'] = [[0, 1]]
rb_circs, xdata = randomized_benchmarking_seq(**rb_opts)

# Run on a noisy simulator
noise_model = NoiseModel()
noise_model.add_all_qubit_quantum_error(depolarizing_error(0.002, 1), ['u1', 'u2', 'u3'])
noise_model.add_all_qubit_quantum_error(depolarizing_error(0.002, 2), 'cx')

backend = qiskit.Aer.get_backend('qasm_simulator')

# Create the RB fitter
rb_fit = RBFitter(None, xdata, rb_opts['rb_pattern'])
for rb_seed,rb_circ_seed in enumerate(rb_circs):

    job = qiskit.execute(rb_circ_seed, backend=backend,
         basis_gates=['u1','u2','u3','cx'],
         noise_model=noise_model)

    # Add data to the fitter
    rb_fit.add_data(job.result())
    print('After seed %d, EPC %f'%(rb_seed,rb_fit.fit[0]['epc']))
